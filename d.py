from stan import wyswietl_stan
from morderstwo import morderstwo
from awans import awans
from patrolowanie import patrolowanie
from trening_strzelecki import trening_strzelecki
from praca import praca, walka, uzyj_kastet, uzyj_palke, uzyj_pistolet
from spolecznosc import spolecznosc, nagrywanie_vloga, vlog_z_interwencji, q_and_a
from aktywnosc_fizyczna import aktywnosc_fizyczna, bieganie, silownia, joga, joga_efekty, poscig_auto, poscig




import random

class Postac:
    def __init__(self, zdrowie=100, energia=100, pieniadze=5000, szczescie=50, zadowolenie_z_pracy=50, umiejetnosci = 0):
        self.zdrowie = zdrowie
        self.energia = energia
        self.pieniadze = pieniadze
        self.szczescie = szczescie
        self.zadowolenie_z_pracy = zadowolenie_z_pracy
        self.umiejetnosci = umiejetnosci

class Bron:
    def __init__(self, nazwa, obrazenia):
        self.nazwa = nazwa
        self.obrazenia = obrazenia

        

class Policjant(Postac):
    def __init__(self):
        super().__init__()
        self.samochod = SamochodPolicjanta("Czarny", "Ford", "123ABC", 4)
        self.bronie = [Bron('Pałka policyjna', 20), Bron('Pistolet paraliżujący', 30), Bron('Kastet', 25)]
        self.liczba_widzow = 0
        self.ogladalnosc = 0
        self.umiejetnosci = 10


class Policjantka(Postac):
    def __init__(self):
        super().__init__()
        self.samochod = SamochodPolicjanta("Biały", "Toyota", "456XYZ", 4)
        self.bronie = [Bron('Pałka policyjna', 20), Bron('Gaz pieprzowy', 25), Bron('Kastet', 25)]
        self.liczba_widzow = 0
        self.ogladalnosc = 0
        self.umiejetnosci = 0



class SamochodPolicjanta:
    def __init__(self, kolor, marka, oznaczenie_sluzbowe, liczba_drzwi):
        self.kolor = kolor
        self.marka = marka
        self.oznaczenie_sluzbowe = oznaczenie_sluzbowe
        self.liczba_drzwi = liczba_drzwi

class SymulatorPolicjanta:
    def __init__(self):
        self.policjant = Policjant()
        self.policjantka = Policjantka()
        self.wybor = {
            '1' : self.praca,
            '2': self.odpoczynek,
            '3': self.spolecznosc,
            '4': self.aktywnosc_fizyczna,
            '5': self.zakupy,
            '6': self.morderstwo,
            '7': self.trening_strzelecki,
            '8': self.patrolowanie,
            '9': self.awans,
            '10': self.sprawdz_stan,
            '11': self.zakoncz_gre
        }
        




    def praca(self):
        praca(self)

    
    def walka(self):
        walka(self)


    def uzyj_kastet(self):
        uzyj_kastet(self)


    def uzyj_palke(self):
        uzyj_palke(self)


    def uzyj_pistolet(self):
        uzyj_pistolet(self)




    def odpoczynek(self):
        print("Masz chwilę wolnego. Co chcesz teraz robić?")
        print("1. Graj w gry.")
        print("2. Czytaj książkę.")
        print("3. Oglądaj film.")
        wybor = input("Wybierz opcję (1, 2 lub 3): ")
        if wybor == '1':
            self.graj_w_gre()
        elif wybor == '2':
            print("Wybrałeś czytanie książki. To świetny sposób na odpoczynek!")
        elif wybor == '3':
            print("Wybrałeś oglądanie filmu. Relaksujące!")
        else:
            print("Nieprawidłowy wybór. Może spróbujesz coś innego?")

    def graj_w_gre(self):
        print("Wybierz grę do zagrania:")
        print("1. Zgadywanie liczby.")
        print("2. Kamień-papier-nożyce.")
        print("3. Wisielec.")
        print("4. Wojna.")
        print("5. Kółko i krzyżyk")
        wybor_gry = input("Wybierz grę (1, 2, 3, 4 lub 5): ")
        if wybor_gry == '1':
            self.zgadywanie_liczby()
        elif wybor_gry == '2':
            self.kamien_papier_nozyce()
        elif wybor_gry == '3':
            self.wisielec()
        elif wybor_gry == '4':
            self.wojna()
        elif wybor_gry == '5':
            self.tictactoe()
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

    def zgadywanie_liczby(self):
        liczba = random.randint(1, 100)
        print("Zgadnij liczbę z zakresu od 1 do 100.")
        proba = 0
        while True:
            proba += 1
            zgadnij = int(input("Zgadnij liczbę: "))
            if zgadnij < liczba:
                print("Za mało!")
            elif zgadnij > liczba:
                print("Za dużo!")
            else:
                print(f"Brawo! Zgadłeś liczbę {liczba} w {proba} próbach.")
                break

    def kamien_papier_nozyce(self):
        wybor_gracza = input("Wybierz: kamień, papier, nożyce: ").lower()
        wybory = ['kamień', 'papier', 'nożyce']
        wybor_komputera = random.choice(wybory)
        print(f"Twój wybór: {wybor_gracza}")
        print(f"Wybor komputera: {wybor_komputera}")
        if wybor_gracza == wybor_komputera:
            print("Remis!")
        elif (wybor_gracza == 'kamień' and wybor_komputera == 'nożyce') or \
                (wybor_gracza == 'papier' and wybor_komputera == 'kamień') or \
                (wybor_gracza == 'nożyce' and wybor_komputera == 'papier'):
            print("Wygrałeś!")
        else:
            print("Przegrałeś!")

    def wisielec(self):
        slowa = ['pies', 'kot', 'samochód', 'komputer', 'telefon']
        slowo = random.choice(slowa)
        dlugosc_slowa = len(slowo)
        ukryte_slowo = ['_' for _ in range(dlugosc_slowa)]
        szanse = 7
        while szanse > 0 and '_' in ukryte_slowo:
            print(" ".join(ukryte_slowo))
            litera = input("Zgadnij literę: ").lower()
            if litera in slowo:
                for i in range(dlugosc_slowa):
                    if slowo[i] == litera:
                        ukryte_slowo[i] = litera
            else:
                szanse -= 1
                print(f"Nie ma takiej litery! Pozostało {szanse} szans.")
        if '_' not in ukryte_slowo:
            print("Brawo! Odgadłeś słowo!")
        else:
            print("Nie udało Ci się odgadnąć słowa. Koniec gry.")

    def wojna(self):
        print("Rozpoczynamy grę w Wojnę!")
        talia = list(range(2, 15)) * 4
        random.shuffle(talia)
        talia_gracza = talia[:26]
        talia_komputera = talia[26:]
        punkty_gracz = 0
        punkty_komputer = 0
        runda = 0
        while len(talia_gracza) > 0 and len(talia_komputera) > 0:
            runda += 1
            karta_gracz = talia_gracza.pop(0)
            karta_komputer = talia_komputera.pop(0)
            print(f"Runda {runda}: Gracz wyciąga {karta_gracz}, a komputer wyciąga {karta_komputer}.")
            if karta_gracz > karta_komputer:
                punkty_gracz += 1
                print("Gracz zdobywa punkt!")
            elif karta_gracz < karta_komputer:
                punkty_komputer += 1
                print("Komputer zdobywa punkt!")
            else:
                print("Remis!")
        if punkty_gracz > punkty_komputer:
            print("Gratulacje! Wygrałeś grę wojna!")
        elif punkty_gracz < punkty_komputer:
            print("Niestety, przegrałeś grę wojna. Spróbuj ponownie!")
        else:
            print("Remis!")



    def tictactoe(self):
        plansza = [[" " for _ in range(3)] for _ in range(3)]
        znaki = ["X", "O"]
        obecny_gracz = 0

        print("Witaj w grze w kółko i krzyżyk!")
        self.wyswietl_plansze(plansza)

        while True:
            print(f"Gracz {obecny_gracz + 1}: Twój ruch")
            if obecny_gracz == 0:
                wiersz = int(input("Wybierz wiersz (0, 1, 2): "))
                kolumna = int(input("Wybierz kolumnę (0, 1, 2): "))
                if 0 <= wiersz <= 2 and 0 <= kolumna <= 2:
                    if self.ruch_gracza(plansza, znaki[obecny_gracz], wiersz, kolumna):
                        self.wyswietl_plansze(plansza)
                        if self.sprawdz_wygrana(plansza, znaki[obecny_gracz]):
                            print(f"Gracz {obecny_gracz + 1} wygrał!")
                            break
                        elif all(pole != " " for wiersz in plansza for pole in wiersz):
                            print("Remis!")
                            break
                        obecny_gracz = (obecny_gracz + 1) % 2
                else:
                    print("Wybierz poprawne wartości dla wiersza i kolumny (0, 1, 2).")
            else:
                self.ruch_bota(plansza, znaki[obecny_gracz])
                self.wyswietl_plansze(plansza)
                if self.sprawdz_wygrana(plansza, znaki[obecny_gracz]):
                    print(f"Bot wygrał!")
                    break
                elif all(pole != " " for wiersz in plansza for pole in wiersz):
                    print("Remis!")
                    break
                obecny_gracz = (obecny_gracz + 1) % 2

    def wyswietl_plansze(self, plansza):
        for wiersz in plansza:
            print(" | ".join(wiersz))
            print("-" * 10)

    def sprawdz_wygrana(self, plansza, znak):
        for wiersz in plansza:
            if all(znak == pole for pole in wiersz):
                return True

        for i in range(3):
            if all(znak == plansza[j][i] for j in range(3)):
                return True

        if all(znak == plansza[i][i] for i in range(3)) or all(znak == plansza[i][2 - i] for i in range(3)):
            return True

        return False

    def ruch_gracza(self, plansza, znak, wiersz, kolumna):
        if plansza[wiersz][kolumna] == " ":
            plansza[wiersz][kolumna] = znak
            return True
        else:
            print("To pole jest już zajęte! Wybierz inne.")
            return False

    def ruch_bota(self, plansza, znak):
        wolne_pola = [(i, j) for i in range(3) for j in range(3) if plansza[i][j] == " "]
        wiersz, kolumna = random.choice(wolne_pola)
        plansza[wiersz][kolumna] = znak
        print(f"Bot wybrał pole: ({wiersz}, {kolumna})")




    def spolecznosc(self):
        spolecznosc(self)


    def nagrywanie_vloga(self):
        nagrywanie_vloga(self)


    def vlog_z_interwencji(self):
        vlog_z_interwencji(self)


    def q_and_a(self):
        q_and_a(self)


    def aktywnosc_fizyczna(self):
        aktywnosc_fizyczna(self)

    
    def bieganie(self):
        bieganie(self)


    def silownia(self):
        silownia(self)

    
    def joga(self):
        joga(self)


    def joga_efekty(self):
        joga_efekty(self)


    def poscig_auto(self):
        poscig_auto(self)


    def posicg(self):
        poscig(self)

   




    def zakupy(self):
        print("Idziesz na zakupy. Wybierz, co chcesz kupić:")
        print("1. Kup coś dla siebie")
        print("2. Kup coś dla partnerki")
        print("3. Zorganizuj wakacje")
        wybor = input("Wybierz opcję (1/2/3): ")
        
        if wybor == '1':
            print("Co chcesz kupić dla siebie?")
            print("1. Nowa kurtka")
            print("2. Sprzęt sportowy")
            print("3. Książki")
            wybor_dla_siebie = input("Wybierz opcję (1/2/3): ")
            
            if wybor_dla_siebie == '1':
                if self.policjant.pieniadze >= 10:
                    self.policjant.pieniadze -= 10
                    print("Kupiłeś nową kurtkę dla siebie. Twoje pieniądze zmniejszyły się o 10.")
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            elif wybor_dla_siebie == '2':
                if self.policjant.pieniadze >= 15:
                    self.policjant.pieniadze -= 15
                    print("Kupiłeś nowy sprzęt sportowy dla siebie. Twoje pieniądze zmniejszyły się o 15.")
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            elif wybor_dla_siebie == '3':
                if self.policjant.pieniadze >= 5:
                    self.policjant.pieniadze -= 5
                    print("Kupiłeś nowe książki dla siebie. Twoje pieniądze zmniejszyły się o 5.")
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            else:
                print("Nie wybrano poprawnej opcji.")
                
        elif wybor == '2':
            print("Co chcesz kupić dla partnerki?")
            print("1. Kwiaty")
            print("2. Perfumy")
            print("3. Biżuteria")
            wybor_dla_partnerki = input("Wybierz opcję (1/2/3): ")
            
            if wybor_dla_partnerki == '1':
                if self.policjant.pieniadze >= 20:
                    self.policjant.pieniadze -= 20
                    print("Kupiłeś kwiaty dla partnerki. Twoje pieniądze zmniejszyły się o 20.")
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            elif wybor_dla_partnerki == '2':
                if self.policjant.pieniadze >= 50:
                    self.policjant.pieniadze -= 50
                    print("Kupiłeś perfumy dla partnerki. Twoje pieniądze zmniejszyły się o 50.")
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            elif wybor_dla_partnerki == '3':
                if self.policjant.pieniadze >= 100:
                    self.policjant.pieniadze -= 100
                    print("Kupiłeś biżuterię dla partnerki. Twoje pieniądze zmniejszyły się o 100.")
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            else:
                print("Nie wybrano poprawnej opcji.")
                
        elif wybor == '3':
            print("Chcesz zorganizować wakacje dla siebie i partnerki.")
            print("1. Wypoczynek nad morzem")
            print("2. Górski raj")
            print("3. Zwiedzanie europejskich miast")
            wybor_wakacji = input("Wybierz opcję (1/2/3): ")
            
            if wybor_wakacji == '1':
                if self.policjant.pieniadze >= 500:
                    self.policjant.pieniadze -= 500
                    print("Zorganizowałeś wakacje nad morzem. Twoje pieniądze zmniejszyły się o 500.")
                    self.wakacje_nad_morzem()
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            elif wybor_wakacji == '2':
                if self.policjant.pieniadze >= 800:
                    self.policjant.pieniadze -= 800
                    print("Zorganizowałeś górski wypoczynek. Twoje pieniądze zmniejszyły się o 800.")
                    self.wakacje_w_gorach()
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            elif wybor_wakacji == '3':
                if self.policjant.pieniadze >= 1000:
                    self.policjant.pieniadze -= 1000
                    print("Zorganizowałeś wakacje w europejskich miastach. Twoje pieniądze zmniejszyły się o 1000.")
                    self.wakacje_w_miastach()
                else:
                    print("Nie masz wystarczająco pieniędzy.")
            else:
                print("Nie wybrano poprawnej opcji.")
                
        else:
            print("Nie wybrano poprawnej opcji.")
            
    def wakacje_nad_morzem(self):
        print("Wybierz kraj, do którego chcesz pojechać:")
        print("1. Hiszpania")
        print("2. Włochy")
        print("3. Grecja")
        wybor_kraju = input("Wybierz opcję (1/2/3): ")
        
        if wybor_kraju == '1':
            print("Wybrałeś Hiszpanię. Cieszysz się pięknymi plażami Costa Brava.")
            self.przygody_nad_morzem("Hiszpania")
        elif wybor_kraju == '2':
            print("Wybrałeś Włochy. Odpoczywasz na plażach Sycylii.")
            self.przygody_nad_morzem("Włochy")
        elif wybor_kraju == '3':
            print("Wybrałeś Grecję. Relaksujesz się na wyspach greckich.")
            self.przygody_nad_morzem("Grecja")
        else:
            print("Nie wybrano poprawnej opcji.")
            
    def wakacje_w_gorach(self):
        print("Wybierz kraj, do którego chcesz pojechać:")
        print("1. Szwajcaria")
        print("2. Austria")
        print("3. Polska")
        wybor_kraju = input("Wybierz opcję (1/2/3): ")
        
        if wybor_kraju == '1':
            print("Wybrałeś Szwajcarię. Zwiedzasz Alpy i cieszysz się pięknymi widokami.")
            self.przygody_w_gorach("Szwajcaria")
        elif wybor_kraju == '2':
            print("Wybrałeś Austrię. Odpoczywasz w Alpach austriackich.")
            self.przygody_w_gorach("Austria")
        elif wybor_kraju == '3':
            print("Wybrałeś Polskę. Spędzasz czas w Tatrach.")
            self.przygody_w_gorach("Polska")
        else:
            print("Nie wybrano poprawnej opcji.")
            
    def wakacje_w_miastach(self):
        print("Wybierz kraj, do którego chcesz pojechać:")
        print("1. Francja")
        print("2. Niemcy")
        print("3. Włochy")
        wybor_kraju = input("Wybierz opcję (1/2/3): ")
        
        if wybor_kraju == '1':
            print("Wybrałeś Francję. Zwiedzasz Paryż, Marsylię i Niceę.")
            self.przygody_w_miastach("Francja")
        elif wybor_kraju == '2':
            print("Wybrałeś Niemcy. Odkrywasz Berlin, Monachium i Hamburg.")
            self.przygody_w_miastach("Niemcy")
        elif wybor_kraju == '3':
            print("Wybrałeś Włochy. Zwiedzasz Rzym, Mediolan i Florencję.")
            self.przygody_w_miastach("Włochy")
        else:
            print("Nie wybrano poprawnej opcji.")
            
    def przygody_nad_morzem(self, kraj):
        if kraj == "Hiszpania":
            print("Odwiedzasz Barcelonę i oglądasz mecz piłki nożnej na Camp Nou.")
            print("Zwiedzasz piękne plaże i kosztujesz lokalnych tapas.")
        elif kraj == "Włochy":
            print("Odwiedzasz zabytkowe miejsca w Rzymie i odpoczywasz na plażach Sycylii.")
            print("Degustujesz wspaniałe włoskie jedzenie i wina.")
        elif kraj == "Grecja":
            print("Zwiedzasz Akropol w Atenach i relaksujesz się na wyspach Santorini.")
            print("Próbujesz lokalnych przysmaków i uczysz się tradycyjnych tańców.")
            
    def przygody_w_gorach(self, kraj):
        if kraj == "Szwajcaria":
            print("Zwiedzasz malownicze miasteczka i spacerujesz po górach.")
            print("Smakujesz lokalne sery i czekoladę.")
        elif kraj == "Austria":
            print("Odwiedzasz piękne jeziora i wędrujesz po alpejskich szlakach.")
            print("Próbujesz tradycyjnych austriackich potraw i napojów.")
        elif kraj == "Polska":
            print("Odwiedzasz Zakopane i wędrujesz po Tatrach.")
            print("Próbujesz oscypka i innych lokalnych specjałów.")
            
    def przygody_w_miastach(self, kraj):
        if kraj == "Francja":
            print("Zwiedzasz Luwr, Wieżę Eiffla i katedrę Notre-Dame.")
            print("Próbujesz francuskich win i serów.")
        elif kraj == "Niemcy":
            print("Odwiedzasz Brandenburską Bramę, Zamek Neuschwanstein i Oktoberfest.")
            print("Smakujesz niemieckie piwo i kiełbaski.")
        elif kraj == "Włochy":
            print("Zwiedzasz Koloseum, Katedrę w Mediolanie i Galerię Uffizi.")
            print("Próbujesz włoskiej pizzy, pasty i gelato.")



    def morderstwo(self):
        morderstwo(self)


 
    def trening_strzelecki(self):
        trening_strzelecki(self)





    def patrolowanie(self):
        patrolowanie(self)




    def awans(self):
        awans(self)



    def sprawdz_stan(self):
        wyswietl_stan(self)

    def zakoncz_gre(self):
        print("Dziękujemy za grę!")
        exit()

    def rozpocznij(self):
        print("Witaj w symulatorze życia policjanta!")
        print("Rozpoczynamy grę...")
        while True:
            print("\nCo chcesz teraz zrobić?")
            print("1. Pracuj")
            print("2. Odpoczywaj")
            print("3. Spędź czas na społecznościach")
            print("4. Ćwicz")
            print("5. Idź na zakupy")
            print("6. Wykonaj przebieg śledztwa")
            print("7. Trening strzelecki")
            print("8. Patroluj ulice")
            print("9. Informacje o awansie")
            print("10. Sprawdź swój stan")
            print("11. Zakończ grę")
            wybor = input("Wybierz opcję (1-11): ")
            if wybor in self.wybor:
                self.wybor[wybor]()
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    symulator = SymulatorPolicjanta()
    symulator.rozpocznij()

