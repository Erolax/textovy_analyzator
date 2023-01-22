oddelovac= "----------------------------------------"

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',
'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

text01 = TEXTS[0].split(" ")
text02 = TEXTS[1].split(" ")
text03 = TEXTS[2].split(" ")

registrovany_uzivatel= {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}

jmeno=input("Username: ")
heslo=input("Password: ")

if registrovany_uzivatel.get(jmeno) == heslo:
    print(oddelovac)
    print(f"Welcome to the app, {jmeno}")
    print("We have 3 texts to be analyzed.")
    print(oddelovac)
else:
    print("unregistered user, terminating the program...")
    quit()

vyber = input("Enter a number btw. 1 and 3 to select text: ")

if not vyber.isnumeric() or int(vyber) not in range(1,4):
    print("The text with that number doesn't exists, terminating the program...")
    quit()
elif vyber == "1":
    vyber = text01
elif vyber == "2":
    vyber = text02
else:
    vyber = text03

upraveny_text = list()

for slovo in vyber:
    upraveny_text.append(slovo.strip(".,:!?").replace("\n",""))

pocet_slov = len(upraveny_text)
print(oddelovac)
print(f"Tehere are {pocet_slov} words in the selected text.")

velke_pismeno = list()

for slovo in vyber:
    if slovo.istitle():
        velke_pismeno.append(slovo)

pocet_slov_velke_pismeno = len(velke_pismeno)
print(f"There are {pocet_slov_velke_pismeno} titlecase words.")

velka_pismena=list()

for slovo in vyber:
    if slovo.isupper() and slovo.isalpha():
        velka_pismena.append(slovo)

pocet_velka_pismena = len(velka_pismena)
print(f"There are {pocet_velka_pismena} uppercase words.")

maly_pismana=list()

for slovo in vyber:
    if slovo.islower():
        maly_pismana.append(slovo)

pocet_malych_pismen = len(maly_pismana)
print(f"Ther are {pocet_malych_pismen} lowercase words.")

cisla=list()

for slovo in vyber:
    if slovo.isnumeric():
        cisla.append(slovo)

pocet_cisel = len(cisla)
print(f"Ther are {pocet_cisel} numeric strings.")

soucet_cisel = list()

for cislo in range(len(cisla)):
    cisla[cislo]=int(cisla[cislo])
suma_cisel=sum(cisla)
print(f"The sum of all the numbers {suma_cisel}")
print(oddelovac)