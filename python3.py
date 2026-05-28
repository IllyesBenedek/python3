#--------------------------
'''
Feladat: Számtani sorozat fájlba írása
Készíts függvényt szaz_szam_fajlba néven, amely 1-tól 100-ig egyesével kiírja a számokat egy fájlba.
Minden szám kerüljön új sorba.
A fájl nevét paraméterként kapja meg a függvény.
'''
def szaz_szam_fajlba(fajnev):
    with open(fajnev, "w")as f:
        for i in range(1, 101):
            f.write(str(i) + "\n")
        
# Ez még nem megy

#--------------------------
'''
Feladat: Utolsó karakter a szövegfájlban
Írj egy függvényt utolso_karakter_a_fajlban néven, amely visszatér egy szövegfájl utolsó karakterével.
A függvény bemenő paramétere a fájl neve.
'''
def utolso_karakter_a_fajlban(fajnev):
    with open(fajnev) as f:
        karakter = f.read()
    if karakter == "":
        return None
    return karakter[-1]


#--------------------------
'''
A leggyakoribb_karakter(fname) függvény
paraméterként egy fájlnevet kap és
visszatér a  fájlban leggyakrabban előforduló karakterrel.
'''
def leggyakoribb_karakter(fajnev):
    with open(fajnev) as f:
        karakter = f.read()
    leggyakoribb = karakter[0]
    for i in karakter:
        if karakter.count(i) > karakter.count(leggyakoribb):
            leggyakoribb = i
    return leggyakoribb
# Ez még nem megy
#--------------------------
'''
Feladat: Leggyakoribb szám a szövegfájlban.
Írj egy függvényt leggyakoribb_szam_a_fajlban néven, amely visszatér a szövegfájlban levő leggyakoribb számmal.
A függvény bemenő paramétere a fájl neve.
'''
def leggyakoribb_szam_a_fajlban(fajnev):
    with open(fajnev, "r") as f:
        szamok = f.read().split()
    leggyakoribb = int(szamok[0])
    for i in szamok:
        if szamok.count(i) > szamok.count(str(leggyakoribb)):
            leggyakoribb = int(i)
    return leggyakoribb
# Ez még nem megy

#--------------------------
'''
Feladat: Legnagyobb szám egy szövegfájlban.
Írj egy függvényt legnagyobb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő legnagyobb számmal.
A függvény bemenő paramétere a fájl neve.
'''
def legnagyobb_szam_a_fajlban(fajnev):
    with open(fajnev) as f:
        lista = f.read().split()
    if lista == []:
        return None
    max = int(lista[0])
    for i in lista:
        if int(i) > max:
            max = int(i)
    return max


#--------------------------
'''
Az r_betuk_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő 'r' betük számával.
'''
def r_betuk_szama(fajnev):   
    with open(fajnev) as f:
          tartalom = f.read()
    db = 0
    for i in tartalom:
        if i == "r":
            db += 1
    return db


#--------------------------
'''
Feladat: Pozitívok egy szövegfájlból.
Írj egy függvényt pozitiv_a_fajlbol néven, amely visszatér a szövegfájlban levő pozitiv számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''
def pozitiv_a_fajlbol(fajnev):
    with open(fajnev) as f:
        pozitivok = f.read().split()
    poz = []
    for i in pozitivok:
        if int(i) > 0:
            poz.append(int(i))
    return poz


#--------------------------
'''
Feladat: Kocka osztály definiálása. 
[Objektumorientált programozás]
Hozz létre egy osztályt Kocka néven.
A Kocka osztály lehetővé teszi a kocka oldalhosszúságának tárolását.
A Kocka osztály rendelkezik egy tefogat() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum térfogatát.
A Kocka osztály rendelkezik egy felszin() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
    visszaadja az adott objektum felszínét.
'''
class Kocka:
    def __init__(self, a):
        self.a = a
    def terfogat(self):
        return self.a ** 3
    def felszin(self):
        return 6 * self.a ** 2


#--------------------------
'''
Feladat: String fájlba írása
A string_fajlba nevű függvény az első paraméterként kapott sztringet fájlba írja.
A fájl nevét második paraméterként kapja meg a függvény.
'''
def string_fajlba(string, fajnev):
    with open(fajnev, "w") as f:
        f.write(string)


#--------------------------
'''
Feladat: Negatív számok száma egy szövegfájlban.
Írj egy függvényt negativ_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő negativ számok számával.
A függvény bemenő paramétere a fájl neve.
'''
def negativ_szamok_szama_a_fajlban(fajnev):
    with open(fajnev) as f:
        negativok = f.read().split()
    neg = 0
    for i in negativok:
        if int(i) < 0:
            neg += 1
    return neg


#--------------------------
'''
Feladat: Páratlan számok száma egy szövegfájlban.
Írj egy függvényt paratlan_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páratlan számok számával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Négyzet osztály definiálása. 
[Objektumorientált programozás]
Hozz létre egy osztályt Negyzet néven.
A Negyzet osztály lehetővé teszi a negyzet oldalhosszúságának tárolását.
A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum kerületét.
A Negyzet osztály rendelkezik egy terulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum területét.
'''



#--------------------------
'''
A sorok_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő sorok számával.
'''



#--------------------------
'''
Feladat: Számok összege egy szövegfájlban.
Írj egy függvényt szamok_osszege_a_fajlban néven amely visszatér egy szövegfájlban levő számok összegével.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Első karakter a szövegfájlban
Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
A karakterek_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő karakterek számával. 
('\n karakterekkel együtt')
'''



#--------------------------
'''
Feladat: Hárommal osztható számok a szövegfájlban.
Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
A leghosszabb_sor_hossza(fname) függvény
paraméterként egy fájlnevet kap és
visszatér a  fájlban levő leghosszabb sor hosszával.
'''



#--------------------------
'''
A lorem_szavak_szama nevű függvény 
paraméterként egy fájlnevet kap és
visszatér a  fájlban levő "lorem" szavak számával.
'''



#--------------------------
'''
Feladat: Legkisebb szám egy szövegfájlban.
Írj egy függvényt legkisebb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő lekisebb számmal.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
A szavak_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő szavak számával.
'''



#--------------------------
'''
Feladat: Páratlanok egy szövegfájlból.
Írj egy függvényt paratlanok_a_fajlbol néven, amely visszatér a szövegfájlban levő páratlan számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Téglalap osztály definiálása. 
[Objektumorientált programozás]
Hozz létre egy osztályt Teglalap néven.
A Teglalap osztály lehetővé teszi a téglalap oldalhosszúságainak tárolását.
A Teglalap osztály rendelkezik egy kerulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum kerületét.
A Teglalap osztály rendelkezik egy terulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum területét.
'''



#--------------------------
'''
Feladat: Párosok egy szövegfájlból.
Írj egy függvényt parosok_a_fajlbol néven, amely visszatér a szövegfájlban levő páros számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Neggyel osztható számok a szövegfájlban.
A neggyel_oszthato_szamok_a_fajlban függvény
egy függvényt neggyel_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő neggyel osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Páros számok száma egy szövegfájlban.
Írj egy függvényt paros_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páros számok számával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Negatívok egy szövegfájlból.
Írj egy függvényt negativok_a_fajlbol néven, amely visszatér a szövegfájlban levő negativ számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Számok átlaga egy szövegfájlban.
Írj egy függvényt szamok_atlaga_a_fajlban néven, amely visszatér egy szövegfájlban levő számok átlagával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Pozitív számok száma egy szövegfájlban.
Írj egy függvényt pozitiv_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő pozitiv számok számával.
A függvény bemenő paramétere a fájl neve.
'''



#======================================================================================================================C:\Users\bened\Downloads\python3