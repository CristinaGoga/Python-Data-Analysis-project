import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('volkswagen.csv', sep=',')
print("1. Citire din fisier csv.")
print(df)
print(df. head())

#2. Tratarea valorilor lipsa
print("\n2. Tratarea valorilor lipsa.")
for col in df.columns:
    if df[col].dtype != object:  # Se calculează media doar pentru coloanele numerice
        mean = df[col].mean()
        df[col].fillna(mean, inplace=True)

# Am verificat daca valorile N/A au fost completate in coloana  Emisii CO2 (g/km)
print(df['Emisii CO2 (g/km)'])


# 3. utilizarea listelor și a dicționarelor, incluzând metode specifice acestora;
#Pentru utilizarea listelor si a metodelor specifice, am realizat 2 liste care descriu mode
#lul de transmisie automat/manual. Rezultatul arata ca exista mai multe masini cu transmisie manuala(29)
#decat cu transmisie automata(21).
print("\n3. Utilizarea listelor")
# crearea listelor cu modelele de masini cu transmisie manuala si automata
modele_manuala = df.loc[df['Transmisie'] == 'Manual', 'Model'].tolist()
modele_automatica = df.loc[df['Transmisie'] == 'Automat', 'Model'].tolist()


# numararea modelelor de masini in fiecare lista
numar_modele_manuala = len(modele_manuala)
numar_modele_automatica = len(modele_automatica)

print("Numarul de modele cu transmisie manuala:", numar_modele_manuala)
print("Numarul de modele cu transmisie automata:", numar_modele_automatica)

print("\n3. Utilizarea dictionarelor")
#In ceea ce priveste crearea unui dictionar, am realizat un top 5 masini care au
#cel mai mare consum in oras. Cheia dictionarului este modelul masinii, iar valoarea
#este consumul mediu in oras. Masina care are cel mai mare consum in oras este ID.3, urmata
# de ID.5, L80, Routan, Phaeton.
# crearea dictionarului cu modelele de masini si consumul mediu in oras

dictionar_consum_oras = {}
for index, row in df.iterrows():
    dictionar_consum_oras[row['Model']] = row['Consum oras (l/100km)']

# sortarea dictionarului in ordine cresc a consumului
dictionar_consum_oras_sortat = dict(sorted(dictionar_consum_oras.items(), key=lambda item: item[1], reverse=False))

# afisarea primelor 5 modele cu cel mai mare consum in oras
print("Cele mai mici 5 consumuri in oras:")
for model, consum_oras in list(dictionar_consum_oras_sortat.items())[:5]:
    print(model, ":", consum_oras, "l/100km")


#4. Utilizarea seturilor și a tuplurilor, incluzând metode specifice acestora;
# cream un set pentru modelele de masini care au evaluarea Euro NCAP >= 4 si emisiile de CO2 <= 120g/km
print("\n4. Utilizarea seturilor")
print("\nMasini cu emisia de CO2<=120g/km si evaluarea NCAP>=4")
masini_set = set(df[(df['Evaluare siguranta (Euro NCAP)'] >= 4) & (df['Emisii CO2 (g/km)'] <= 120)]['Model'])

# afisam preturile acestor modele de masini
for index, row in df.iterrows():
    if row['Model'] in masini_set:
        print(row['Model'], row['Pret (lei)'])

# 4. Utilizarea tuplurilor

print("\n4. Utilizarea tuplurilor")
# Selectăm mașinile care au avut o evaluare de siguranță de cel puțin 4 stele Euro NCAP
df_filtered = df[(df['Evaluare siguranta (Euro NCAP)'] >= 4)]

# Sortăm mașinile în ordinea descrescătoare a puterii
df_sorted = df_filtered.sort_values(by=['Putere (CP)'], ascending=False)

# Calculăm costul total anual (întreținere + asigurare) pentru fiecare mașină
df_sorted['Cost total anual'] = df_sorted['Cost intretinere (lei/an)'] + df_sorted['Cost asigurare (lei/an)']

# Afișăm mașinile selectate, însoțite de informațiile cerute, sub formă de tupluri
cars = []
for index, row in df_sorted.iterrows():
    car = (row['Model'], row['Putere (CP)'], row['Evaluare siguranta (Euro NCAP)'], row['Cost total anual'])
    cars.append(car)

for car in cars:
    print(car)




#Utilizare Set-uri

# Cream un set cu toate modelele
all_models = set(df['Model'])


print("\n5.6.7. Utilizarea unei functii + if + for")
def numara_masini_an_prod(set_date):
    contor_mai_mic = 0
    contor_mai_mare = 0
    for index, rand in set_date.iterrows():
        if rand['Anul producției'] < 2015:
            contor_mai_mic += 1
        elif rand['Anul producției'] > 2015:
            contor_mai_mare += 1
    return contor_mai_mic, contor_mai_mare

contor_mai_mic, contor_mai_mare = numara_masini_an_prod(df)
print("\nNumărul de mașini cu anul producției mai mic de 2015: {}".format(contor_mai_mic))
print("Numărul de mașini cu anul producției mai mare de 2015: {}".format(contor_mai_mare))

print("\n8. Utilizarea loc si iloc")
#loc si iloc

# Găsirea mașinii cu cel mai mare motor
masina_max_motor = df.loc[df['Cilindree (cc)'].idxmax()]
# Găsirea mașinii cu cel mai mic motor
index_masina_min_motor = df['Cilindree (cc)'].idxmin()
masina_min_motor = df.iloc[index_masina_min_motor]
# Afișarea informațiilor dorite
print("\nMașina cu cel mai mare motor:")
print("Model: ", masina_max_motor['Model'])
print("Motor: ", masina_max_motor['Cilindree (cc)'])
print("Anul producție: ", masina_max_motor['Anul producției'])
print()
print("Mașina cu cel mai mic motor:")
print("Model: ", masina_min_motor['Model'])
print("Motor: ", masina_min_motor['Cilindree (cc)'])
print("Anul producție: ", masina_min_motor['Anul producției'])


print("\n9.Modificarea datelor în pachetul pandas ")

#modificarea datelor în pachetul pandas;
print()
# Multiplicarea valorilor din coloana "Pret (lei)" cu 4.90
df['Pret (lei)'] = df['Pret (lei)'] / 4.90

# Redenumirea coloanei "Pret (lei)" în "Pret (Euro)"
df = df.rename(columns={'Pret (lei)': 'Pret (Euro)'})

# Afișarea DataFrame-ului modificat
print(df['Pret (Euro)'].round(2))
print(df['Pret (Euro)'].head(3).round(2))

# Utilizare functii de grup

# Găsiți consumul mediu de combustibil pe autostradă și în oraș pentru mașinile cu transmisie automată
auto_cities = df[df["Transmisie"] == "Automat"].groupby("Model")[["Consum oras (l/100km)",
                                                                  "Consum autostrada (l/100km)"]].mean()
print("Consumul mediu masini automate:")
print(auto_cities)


#Grupati masinile in functie de anul fabricatiei si faceti media preturilor pentru fiecare an de fabricatie
df_grouped_an = df.groupby('Anul producției')['Pret (Euro)'].mean()
print("Preturile masinilor grupate dupa anul fabricatiei")
print(df_grouped_an)

#utilizare merge

df_caroserii = pd.read_csv('caroserii.csv', sep=',')
print("1. Citire din fisier csv.")
print(df_caroserii)
print(df_caroserii. head())

# folosim functia merge pentru a combina cele doua seturi de date
df_merged = pd.merge(df, df_caroserii, on="Model")

# afisam rezultatul
print(df_merged)


#Stergerea coloanelor

# Stergem coloana "Dimensiuni"
df1 = df.drop(columns=['Dimensiuni (lungime x latime x inaltime)'])

#Stergere inregistrari

# identificam indecsii randurilor care contin modelele Type 2, Type 3 si Type 4
drop_indices = df[(df['Model'] == 'Type 2 (Kombi)') | (df['Model'] == 'Type 3') | (df['Model'] == 'Type 4')].index

# stergem randurile folosind functia drop
df.drop(drop_indices, inplace=True)
print(df.head())

# reprezentare graficaS

#sa se afiseze grafic o reprezentare in care se evidentiaza costul asigurarii
# in functie de marimea motorului pentru fiecare model de masina

#extragem coloanele cost asigurare si cilindree
cost_asig = df['Cost asigurare (lei/an)']
motor = df['Cilindree (cc)']

#cream graficul
plt.scatter(cost_asig, motor)

#setam titlul si etichetele axelor
plt.title('Costul asigurarii in functie de marimea motorului')
plt.xlabel('Cost asigurare (lei)')
plt.ylabel('Marime motor(cc)')

#afisam graficul
plt.show()








