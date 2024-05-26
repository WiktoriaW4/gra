import random

def aktywnosc_fizyczna(self):
        print("Czas na aktywność fizyczną!")
        print("1. Bieganie.")
        print("2. Siłownia.")
        print("3. Joga.")
        wybor = input("Wybierz opcję (1, 2 lub 3): ")
        if wybor == '1':
            self.bieganie()
        elif wybor == '2':
            self.silownia()
        elif wybor == '3':
            self.joga()
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
    
def bieganie(self):
        print("Rozpoczynamy bieganie!")
        dystans = int(input("Ile kilometrów chcesz przebiec? "))
        self.policjant.energia -= dystans * 2
        self.policjant.zdrowie += dystans // 2
        self.policjant.szczescie += dystans // 3
        print(f"Przebiegłeś {dystans} kilometrów. Odczuwasz zmęczenie, ale także satysfakcję z wysiłku.")

       
        if random.random() < 0.1:  
            print("Po bieganiu pojawia się nagła akcja! Rozpoczyna się pościg!")
            if self.poscig():
                print("Złoczyńca złapany!")
                self.policjant.szczescie += 30
            else:
                print("Złoczyńca uciekł.")
                self.policjant.energia -= 50
                self.policjant.zdrowie -= 20

def silownia(self):
        print("Rozpoczynamy trening na siłowni!")
        print("Wybierz partie mięśni, którą chcesz ćwiczyć:")
        print("1. Klatka piersiowa")
        print("2. Plecy")
        print("3. Nogi")
        print("4. Barki")
        print("5. Ramiona")
        wybor_partii = input("Wybierz numer: ")
        liczba_serii = int(input("Podaj liczbę serii: "))
        liczba_powtorzen = int(input("Podaj liczbę powtórzeń na serię: "))
        self.policjant.energia -= liczba_serii * liczba_powtorzen * 2
        self.policjant.zdrowie += liczba_serii * liczba_powtorzen // 2
        self.policjant.szczescie += liczba_serii * liczba_powtorzen // 3
        print(f"Wykonujesz {liczba_serii} serii po {liczba_powtorzen} powtórzeń dla wybranej partii mięśni.")

        
        print("Wychodzisz z siłowni, kiedy nagle dostrzegasz pędzące auto!")
        if self.poscig_auto():
            print("Pościg udany! Złoczyńca złapany!")
            self.policjant.szczescie += 30
        else:
            print("Złoczyńca uciekł.")
            self.policjant.energia -= 50
            self.policjant.zdrowie -= 20

def joga(self):
        print("Rozpoczynamy praktykę jogi!")
        print("Wybierz długość trwania sesji jogi:")
        print("1. Krótka (15 minut).")
        print("2. Średnia (30 minut).")
        print("3. Długa (45 minut).")
        wybor = input("Wybierz opcję (1, 2 lub 3): ")
        
     
        if wybor == '1':
            self.joga_efekty(15, "krótką")
        elif wybor == '2':
            self.joga_efekty(30, "średnią")
        elif wybor == '3':
            self.joga_efekty(45, "długą")
        else:
            print("Nieprawidłowy wybór.")
        
    
        if random.random() < 0.1: 
            print("Po praktyce jogi pojawia się nagła akcja! Rozpoczyna się pościg!")
            if self.poscig():
                print("Złoczyńca złapany!")
                self.policjant.szczescie += 30
            else:
                print("Złoczyńca uciekł.")
                self.policjant.energia -= 50
                self.policjant.zdrowie -= 20

def joga_efekty(self, czas, opis):
        print(f"Wybrano {opis} sesję jogi, trwającą {czas} minut.")
        self.policjant.zdrowie += 5
        self.policjant.energia -= 5
        self.policjant.szczescie += 10
        
def poscig_auto(self):
        print("Widzisz pędzące auto! Co robisz?")
        print("1. Załapujesz się do samochodu i ruszasz w pościg.")
        print("2. Próbujesz zastawić pułapkę na drodze, żeby zatrzymać przestępcę.")
        decyzja = input("Wybierz opcję (1 lub 2): ")
        if decyzja == '1':
            if random.random() < 0.5: 
                print("Udało ci się zatrzymać przestępcę!")
                return True
            else:
                print("Niestety, przestępca uciekł.")
                return False
        elif decyzja == '2':
            if random.random() < 0.3: 
                print("Pułapka zadziałała! Złoczyńca zatrzymany!")
                return True
            else:
                print("Pułapka nie powiodła się. Przestępca uciekł.")
                return False
        else:
            print("Nieprawidłowy wybór.")
            return False

def poscig(self):
   
        print("Jesteś w pościgu! Złoczyńca ucieka ulicami miasta.")
        decyzja = input("Czy chcesz kontynuować pościg? (t/n): ")
        if decyzja.lower() == 't':
            if random.random() < 0.5:
                print("Udało ci się złapać przestępcę!")
                return True
            else:
                print("Niestety, przestępca uciekł.")
                return False
        else:
            print("Przerywasz pościg.")
            return False