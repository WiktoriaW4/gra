import random


def praca(self):
        print("Jedziesz na służbę. Podczas patrolowania widzisz agresywną osobę!")
        print("Masz teraz dwie opcje:")
        print("1. Zmierz się z nią i spróbuj ją powstrzymać.")
        print("2. Wezwij wsparcie i czekaj na pomoc.")
        wybor = input("Wybierz opcję (1 lub 2): ")
        if wybor == '1':
            self.walka()
        elif wybor == '2':
            print("Wezwano wsparcie. Trzymaj się z dala od agresywnej osoby, dopóki pomoc nie nadejdzie.")
        else:
            print("Nieprawidłowy wybór. Tracisz cenny czas!")
            self.policjant.zdrowie -= random.randint(5, 15)
            self.policjant.energia -= random.randint(5, 10)

def walka(self):
        bronie = {
            '1': {'nazwa': 'Pałka policyjna', 'obrazenia': 20, 'funkcja': self.uzyj_palke},
            '2': {'nazwa': 'Pistolet paraliżujący', 'obrazenia': 30, 'funkcja': self.uzyj_pistolet},
            '3': {'nazwa': 'Kastet', 'obrazenia': 25, 'funkcja': self.uzyj_kastet}
        }
        wybrana_bron = input("Wybierz broń do walki (1-Pałka, 2-Pistolet, 3-Kastet): ")
        if wybrana_bron in bronie:
            bron = bronie[wybrana_bron]
            bron['funkcja']()
        else:
            print("Nieprawidłowy wybór broni. Tracisz cenny czas!")
            self.policjant.zdrowie -= random.randint(5, 10)
            self.policjant.energia -= random.randint(5, 10)

def uzyj_palke(self):
        agresywna_osoba = 100
        while agresywna_osoba > 0:
            atak = input("Wybierz atak (1-Uderzenie, 2-Odepchnięcie, 3-Trick): ")
            if atak == '1':
                obrazenia = random.randint(15, 25)
                agresywna_osoba -= obrazenia
                print(f"Uderzasz pałką, zadając {obrazenia} obrażeń.")
            elif atak == '2':
                obrazenia = random.randint(10, 20)
                agresywna_osoba -= obrazenia
                print(f"Odepchnąłeś agresywną osobę, zadając {obrazenia} obrażeń.")
            elif atak == '3':
                obrazenia = random.randint(20, 30)
                agresywna_osoba -= obrazenia
                print(f"Wykonujesz bolesny trick pałką, zadając {obrazenia} obrażeń.")
            else:
                print("Nieprawidłowy atak. Tracisz cenny czas!")
                self.policjant.zdrowie -= random.randint(5, 10)
                self.policjant.energia -= random.randint(5, 10)
            if agresywna_osoba <= 0:
                print("Udało Ci się powstrzymać agresywną osobę!")
                self.policjant.szczescie += random.randint(10, 20)
            else:
                self.policjant.zdrowie -= random.randint(10, 20)
                print(f"Agresywna osoba atakuje Cię! Tracisz {random.randint(10, 20)} punktów zdrowia.")

def uzyj_pistolet(self):
        agresywna_osoba = 100
        while agresywna_osoba > 0:
            atak = input("Wybierz atak (1-Strzał w nogę, 2-Strzał w tułów, 3-Strzał w głowę): ")
            if atak == '1':
                obrazenia = random.randint(25, 30)
                agresywna_osoba -= obrazenia
                print(f"Strzelasz w nogi, zadając {obrazenia} obrażeń.")
            elif atak == '2':
                obrazenia = random.randint(30, 35)
                agresywna_osoba -= obrazenia
                print(f"Strzelasz w tułów, zadając {obrazenia} obrażeń.")
            elif atak == '3':
                obrazenia = random.randint(50, 60)
                agresywna_osoba -= obrazenia
                print(f"Strzeliłeś w głowę, zadając {obrazenia} obrażeń.")
            else:
                print("Nieprawidłowy atak. Tracisz cenny czas!")
                self.policjant.zdrowie -= random.randint(5, 10)
                self.policjant.energia -= random.randint(5, 10)
            if agresywna_osoba <= 0:
                print("Udało Ci się powstrzymać agresywną osobę!")
                self.policjant.szczescie += random.randint(10, 20)
            else:
                self.policjant.zdrowie -= random.randint(10, 20)
                print(f"Agresywna osoba atakuje Cię! Tracisz {random.randint(10, 20)} punktów zdrowia.")

def uzyj_kastet(self):
        agresywna_osoba = 100
        while agresywna_osoba > 0:
            atak = input("Wybierz atak (1-Uderzenie proste, 2-Uderzenie podbródkowe, 3-Rzut): ")
            if atak == '1':
                obrazenia = random.randint(15, 25)
                agresywna_osoba -= obrazenia
                print(f"Uderzasz szybko kastetem, zadając {obrazenia} obrażeń.")
            elif atak == '2':
                obrazenia = random.randint(30, 35)
                agresywna_osoba -= obrazenia
                print(f"Uderzasz agresywną osobę silnym ciosem, zadając {obrazenia} obrażeń.")
            elif atak == '3':
                obrazenia = random.randint(25, 35)
                agresywna_osoba -= obrazenia
                print(f"Rzucasz kastetem, zadając {obrazenia} obrażeń.")
            else:
                print("Nieprawidłowy atak. Tracisz cenny czas!")
                self.policjant.zdrowie -= random.randint(5, 10)
                self.policjant.energia -= random.randint(5, 10)
            if agresywna_osoba <= 0:
                print("Udało Ci się powstrzymać agresywną osobę!")
                self.policjant.szczescie += random.randint(10, 20)
            else:
                self.policjant.zdrowie -= random.randint(10, 20)
                print(f"Agresywna osoba atakuje Cię! Tracisz {random.randint(10, 20)} punktów zdrowia.")