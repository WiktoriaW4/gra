import random 

def patrolowanie(self):
        print("Idziesz patrolować miasto.")
        print("Wybierz obszar patrolu:")
        print("1 - Centrum")
        print("2 - Przedmieścia")
        wybor_patrol = input("Wybierz 1 lub 2 - ")

        if wybor_patrol == '1':
            print("Patrolujesz centrum miasta.")
            self.policjant.energia -= 10
            wynik = random.randint(1, 100)
            if wynik > 70:
                print("Udało ci się udaremnić przestępstwo!")
                self.policjant.szczescie += 15
                self.policjant.umiejetnosci += 2
            else:
                print("Nic się nie wydarzyło.")
        elif wybor_patrol == '2':
            print("Patrolujesz przedmieścia.")
            self.policjant.energia -= 5
            wynik = random.randint(1, 100)
            if wynik > 50:
                print("Udało ci się złapać przestępcę!")
                self.policjant.szczescie += 10
                self.policjant.umiejetnosci += 3
            else:
                print("Nic się nie wydarzyło.")
        else:
            print("Zły wybór!")