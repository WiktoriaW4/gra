import random

def spolecznosc(self):
        print("Spotykasz się ze znajomymi. Dobrze porozmawiać po służbie.")
        self.policjant.energia -= 10
        self.policjant.szczescie += 20
        self.policjant.pieniadze -= 15

        wydarzenie = random.choice([
            "Podczas rozmowy dowiadujesz się o interesującej sprawie kryminalnej.",
            "Ktoś z twoich znajomych zaprasza cię na darmowy obiad.",
            "Spotykasz przypadkowo swojego szefa, kto wie, co może to oznaczać?",
            "Podczas spotkania dostajesz telefon od kolegi z pracy z prośbą o wsparcie w ważnej sprawie.",
            "Znajomi opowiadają ci dowcip, który rozbawia całą grupę."
        ])

        print(wydarzenie)

        if self.policjant.szczescie > 50:
            print("Spotkanie było bardzo udane. Czujesz się świetnie!")
            self.policjant.szczescie += 10
        elif self.policjant.szczescie > 30:
            print("Spotkanie poprawiło twój nastrój.")
            self.policjant.szczescie += 5
        elif self.policjant.szczescie > 10:
            print("Niestety, rozmowa nie przebiegła tak dobrze, jakbyś sobie życzył.")
            self.policjant.szczescie -= 5
        else:
            print("Spotkanie było dla ciebie trudne. Czujesz się źle.")
            self.policjant.szczescie -= 10

        print("Możesz teraz napisać wpis na forum.")
        wpis = input("Napisz swój wpis: ")
        print("Twój wpis został opublikowany na forum.")

        print("Przeglądasz najnowsze informacje.")
        informacje = [
            "Nowa ustawa przeciwdziałająca przestępczości została uchwalona.",
            "Pojawiła się informacja o zaginięciu młodej osoby. Policja prosi o pomoc w poszukiwaniach.",
            "Nastąpiła zmiana na stanowisku komendanta lokalnej jednostki policji."
        ]
        print(random.choice(informacje))

        print("Idziesz na przerwę na obiad.")
        print("Wybierz, co chcesz zjeść:")
        print("1. Spaghetti")
        print("2. Pizza")
        print("3. Sałatka")
        wybor_jedzenia = input("Wybierz jedzenie (1/2/3): ")

        if wybor_jedzenia == '1':
            print("Doskonały wybór! Dziś na obiad jest spaghetti.")
        elif wybor_jedzenia == '2':
            print("Pizza to zawsze dobry wybór!")
        elif wybor_jedzenia == '3':
            print("Sałatka jest lekka i zdrowa.")
        else:
            print("Nie wybrano poprawnej opcji.")

  
        print("Otrzymujesz wiadomość od swojego kolegi z pracy.")
        wiadomosc = input("Otworzyć wiadomość? (tak/nie): ")

        if wiadomosc.lower() == 'tak':
            print("Twój kolega prosi o pomoc w rozwiązaniu tajemniczego zagadnienia. Przyjmujesz zadanie?")
            odpowiedz = input("Tak czy nie? ")
            if odpowiedz.lower() == 'tak':
                print("Przyjąłeś zadanie. Rozpoczynasz śledztwo.")
            else:
                print("Odmówiłeś pomocy. Może innym razem.")
        
        print("Spotkanie zakończone.")

        print("Co chcesz zrobić teraz?")
        print("1. Nagrywać vloga")
        print("2. Wracać do domu")
        wybor = input("Wybierz opcję (1 lub 2): ")
        if wybor == '1':
            self.nagrywanie_vloga()
        elif wybor == '2':
            print("Wracasz do domu.")
        else:
            print("Nieprawidłowy wybór. Wracasz do bazy.")

def nagrywanie_vloga(self):
        print("Co chcesz nagrać?")
        print("1. Vlog z interwencji")
        print("2. Q&A")
        wybor_vloga = input("Wybierz opcję (1 lub 2): ")
        if wybor_vloga == '1':
            self.vlog_z_interwencji()
        elif wybor_vloga == '2':
            self.q_and_a()
        else:
            print("Nie wybrano poprawnej opcji.")

def vlog_z_interwencji(self):
        print("Nagrywasz vlog z interwencji.")
        self.policjant.liczba_widzow += random.randint(50, 100)
        self.policjant.ogladalnosc += random.randint(20, 50)
        print(f"Liczba widzów wzrosła do: {self.policjant.liczba_widzow}")
        print(f"Oglądalność wzrosła do: {self.policjant.ogladalnosc}")

def q_and_a(self):
        print("Nagrywasz Q&A.")
        temat = input("Podaj temat Q&A: ")
        print(f"Zaczynasz nagrywać Q&A na temat: {temat}")
        pytania = [
            "Najbardziej brutalna sprawa, jaką zobaczyłeś ?",
            "Czy to prawda, że policja ma dużo wolnego czasu?",
            "Jakie są najczęstsze zagrożenia w pracy policjanta?",
            "Jaka jest najtrudniejsza sprawa, z którą się spotkałeś?",
            "Jakie umiejętności są najważniejsze dla policjanta?"
        ]
        for pytanie in pytania:
            print(f"Pytanie od widza: {pytanie}")
            odpowiedz = input("Twoja odpowiedź: ")
            print("Dzięki za odpowiedź!")
            self.policjant.liczba_widzow += random.randint(5, 15)
            self.policjant.ogladalnosc += random.randint(5, 20)
        print(f"Liczba widzów wzrosła do: {self.policjant.liczba_widzow}")
        print(f"Oglądalność wzrosła do: {self.policjant.ogladalnosc}")
