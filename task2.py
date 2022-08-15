#práce se řetězci
print("What is your favourite movie?")

#délka
#__len__
print("What is your favourite movie?".__len__(), " __len__")
#len()
print(len("What is your favourite movie?"), "   len()")
#split()
print("What is your favourite movie?".split(),"     split()")
print("What is your favourite movie?".split("is"), "    split(is)")
#count()
print("What is your favourite movie?".count("a"), "     count(a)")
#find()
print("What is your favourite movie?".find("h"), "     find(h)")
#startwith()
print("What is your favourite movie?".startswith("W"), "  startwith(W)")
#endswith()
print("What is your favourite movie?".endswith("e"), " endswith(e)")
#isdigit()
print("What is your favourite movie?".isdigit(), " isdigit")
#isalpha()
print("What is your favourite movie?".isalpha(), " isalpha()")
#isupper()
print("What is your favourite movie?".isupper(), " isupper()")
#islower()
print("What is your favourite movie?".islower(), " islower()")

promena = "What is your favourite movie"

#datove typy
#str/řetězec
retezec = "retezec"
retezec = """retezec"""#zanechá formátování
#int/číslo
cislo = 12   #normal
cislo = -1   #záporná

#float/des. číslo
cislo = 1,2  #desetiná
#bool(ean)
ert = False
art = True
asd = 7 > 6   #True


#type()
cislo = input("Zadej číslo: ")
print(type(cislo), " type(cislo)+před str>int")
##str > int
cislo = int(cislo)
print(type(cislo), " type(cislo)+po str>int")

#postavu  - jmeno, příjmení, věk, phlaví, náridnost
jmeno = input("Zdaej jméno\n")
prijmeni = input("Zadej příjmení\n")
vek = input("Zadej věk\n")
pohlavi = input("Zadej tvoje pohlaví\n")
narodnost = input("Zadej tvoji národnost\n")
print("Jmenuji se ", jmeno,prijmeni, "je mi", vek, "let, jsem ",pohlavi, "pochazím z ", narodnost)
print(f"Jmenuji se {jmeno} {prijmeni} je mi {vek} let, jsem {pohlavi} a pochazím z {narodnost}")

#matematické operace
#sciani
sitani = 2 + 3
#odcitani
odcitani  = 3 - 2
#násobení
nasobeni = 2 * 3
#deleni
deleni1 = 7 / 3 #normalni
deleni2 = 7 // 3
print(f"{deleni1}\n{deleni2}")
#mdoulo %/ zbytek po deleni
modulo = 8 % 3 #zbytek po deleni
print(modulo)
#mocniny
mocnina = 2 ** 2
print(mocnina)
#__floor__ zaokrouhlení nahoru
print(2.3.__floor__())
#__round__zaokrouhlení nahoru
print(2.3.__round__)
#kontrola inputu
cislo1 = int(input("zdej číslo1"))
cislo2 = int(input("zdej číslo2"))

print(f"Součet {cislo1 + cislo2}")#součet
print(f"rozdíl {cislo1 - cislo2}")#rozdíl
print(f"násobení {cislo1*cislo2}")#násobení
print(f"dělění {cislo1 / cislo2}")#dělení