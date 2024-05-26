import random


def trening_strzelecki(self):
        print("Wybierasz się na trening strzelecki.")
        print("Chcesz iść sam czy ze swoją partnerką - policjantką?")
        print("Sam - 1,   Z policjantką - 2")
        wybor_1 = input("Wybierz 1 lub 2 - ")

        if wybor_1 == '1':
            print("Idziesz sam na strzelnicę.")
            self.policjant.szczescie -= 5
            print("Wybierz rodzaj broni, której chcesz użyć:")
            print("1 - Pałka policyjna")
            print("2 - Pistolet paraliżujący")
            print("3 - Kastet")
            wybor_bron = input("Wybierz 1, 2 lub 3 - ")

            if wybor_bron == '1':
                print("Trenujesz z pałką policyjną.")
                self.policjant.zdrowie += 5
                self.policjant.umiejetnosci += 1
            elif wybor_bron == '2':
                print("Trenujesz z pistoletem paraliżującym.")
                self.policjant.zdrowie += 10
                self.policjant.umiejetnosci += 2
            elif wybor_bron == '3':
                print("Trenujesz z kastetem.")
                self.policjant.zdrowie += 7
                self.policjant.umiejetnosci += 1
            else:
                print("Zły wybór! Trening nie przyniósł efektów.")

        elif wybor_1 == '2':
            print("Idziesz na strzelnicę ze swoją partnerką.")
            self.policjant.szczescie += 10
            self.policjantka.szczescie += 10

            print("Wybierz rodzaj broni, której chcesz użyć:")
            print("1 - Pałka policyjna")
            print("2 - Pistolet paraliżujący")
            print("3 - Kastet")
            wybor_bron = input("Wybierz 1, 2 lub 3 - ")

            if wybor_bron == '1':
                print("Trenujesz z pałką policyjną.")
                self.policjant.zdrowie += 5
                self.policjant.umiejetnosci += 1
            elif wybor_bron == '2':
                print("Trenujesz z pistoletem paraliżującym.")
                self.policjant.zdrowie += 10
                self.policjant.umiejetnosci += 2
            elif wybor_bron == '3':
                print("Trenujesz z kastetem.")
                self.policjant.zdrowie += 7
                self.policjant.umiejetnosci += 1
            else:
                print("Zły wybór! Trening nie przyniósł efektów.")

            print("Twoja partnerka proponuje konkurs strzelecki. Zgadzasz się?")
            print("Tak - 1,   Nie - 2")
            wybor_2 = input("Wybierz 1 lub 2 - ")

            if wybor_2 == '1':
                print("Zgodziłeś się na konkurs strzelecki.")
                wynik = random.randint(1, 100)
                if wynik > 70:
                    print("Wygrałeś konkurs! Twoje umiejętności strzeleckie wzrosły.")
                    self.policjant.szczescie += 10
                    self.policjant.zadowolenie_z_pracy += 5
                    self.policjant.umiejetnosci += 3
                else:
                    print("Przegrałeś konkurs. Ale było fajnie!")
                    self.policjant.szczescie += 5
            else:
                print("Odmówiłeś konkursu. Trening zakończył się spokojnie.")
        else:
            print("Zły wybór!")
