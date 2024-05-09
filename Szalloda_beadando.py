from abc import ABC, abstractmethod
from datetime import date

# Szoba absztrakt osztály
class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

# Egyágyas és Kétágyas szobák
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # például 15,000 Ft éjszakánként

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 25000)  # például 25,000 Ft éjszakánként

# Szálloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def add_foglalas(self, foglalas):
        self.foglalasok.append(foglalas)

# Foglalás osztály
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

# Foglalás kezelő funkciók
def foglal(szalloda, szobaszam, datum):
    if datum <= date.today():
        raise ValueError("A dátum a múltban van!")
    for foglalas in szalloda.foglalasok:
        if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
            raise ValueError("A szoba ezen a napon már foglalt!")
    for szoba in szalloda.szobak:
        if szoba.szobaszam == szobaszam:
            uj_foglalas = Foglalas(szoba, datum)
            szalloda.add_foglalas(uj_foglalas)
            return uj_foglalas.szoba.ar
    raise ValueError("A szoba nem létezik!")

def lemondas(szalloda, szobaszam, datum):
    for foglalas in szalloda.foglalasok:
        if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
            szalloda.foglalasok.remove(foglalas)
            return True
    return False

def listaz_foglalasok(szalloda):
    for foglalas in szalloda.foglalasok:
        print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.szoba.ar} Ft")

# Felhasználói interfész
def felhasznaloi_interfesz():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.add_szoba(EgyagyasSzoba(101))
    szalloda.add_szoba(KetagyasSzoba(102))
    szalloda.add_szoba(KetagyasSzoba(103))

    while True:
        print("\nVálasszon a következő opciók közül:")
        print("1 - Foglalás")
        print("2 - Lemondás")
        print("3 - Foglalások listázása")
        print("4 - Kilépés")
        print("5 - Szobák listázása")
        valasz = input("Kérem válasszon egy opciót: ")
        if valasz == "4":
            break
        elif valasz == "1":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            ev = int(input("Év: "))
            honap = int(input("Hónap: "))
            nap = int(input("Nap: "))
            datum = date(ev, honap, nap)
            try:
                ar = foglal(szalloda, szobaszam, datum)
                print(f"A foglalás sikeres, az ár: {ar} Ft")
            except Exception as e:
                print(e)
        elif valasz == "2":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            ev = int(input("Év: "))
            honap = int(input("Hónap: "))
            nap = int(input("Nap: "))
            datum = date(ev, honap, nap)
            if lemondas(szalloda, szobaszam, datum):
                print("A lemondás sikeres.")
            else:
                print("Nem található ilyen foglalás.")
        elif valasz == "3":
            if szalloda.foglalasok:
                listaz_foglalasok(szalloda)
            else:
                print("Még nem foglaltak szobát.")
        elif valasz == "5":
            print("Rendelkezésre álló szobák:")
            for szoba in szalloda.szobak:
                if isinstance(szoba, EgyagyasSzoba):
                    print(f"Szobaszám: {szoba.szobaszam} - Egyágyas szoba - Ár: {szoba.ar} Ft")
                elif isinstance(szoba, KetagyasSzoba):
                    print(f"Szobaszám: {szoba.szobaszam} - Kétágyas szoba - Ár: {szoba.ar} Ft")

if __name__ == "__main__":
    felhasznaloi_interfesz()