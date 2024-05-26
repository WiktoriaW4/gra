def morderstwo(self):
        print("Otrzymujesz wezwanie do miejsca zbrodni. Dowiedz się więcej szczegółów o zabójstwie.")
        
        self.policjant.energia -= 20
        if self.policjant.energia <= 0 or self.policjant.zdrowie <= 0:
            print("Niestety, nie masz już energii lub zdrowia. Gra skończona.")
            return
        
        print("Na miejscu zbrodni znajdujesz kilka ważnych elementów:")
        print("1. Narzędzie zbrodni")
        print("2. Ślady krwi")
        print("3. Zeznania świadków")
        wybor_pierwszy = input("Co chcesz zbadać najpierw? (1/2/3): ")
        
        if wybor_pierwszy == '1':
            print("Znalezione narzędzie zbrodni to nóż. Na ostrzu są ślady krwi.")
            print("Czy chcesz przeprowadzić testy DNA na krwi? (tak/nie): ")
            test_dna = input()
            if test_dna.lower() == 'tak':
                self.policjant.pieniadze -= 10
                print("Przeprowadzasz testy DNA. Wyniki wskazują na osobę z przeszłością kryminalną.")
                print("Ślad prowadzi do lokalnego gangu.")
            else:
                print("Decydujesz się nie przeprowadzać testów DNA.")
            
        elif wybor_pierwszy == '2':
            print("Ślady krwi prowadzą do wyjścia z budynku.")
            print("Czy chcesz podążać za śladami? (tak/nie): ")
            sledz_slady = input()
            if sledz_slady.lower() == 'tak':
                self.policjant.energia -= 10
                print("Ślady krwi prowadzą cię do opuszczonego magazynu.")
                print("W magazynie znajdujesz podejrzanego.")
                print("Rozpoczynasz pościg i po krótkiej gonitwie udaje ci się go zatrzymać.")
            else:
                print("Decydujesz się nie podążać za śladami.")
            
        elif wybor_pierwszy == '3':
            print("Zeznania świadków wskazują na podejrzanego, który opuścił miejsce zbrodni krótko po zajściu.")
            print("Czy chcesz przesłuchać świadków? (tak/nie): ")
            przesluchaj = input()
            if przesluchaj.lower() == 'tak':
                self.policjant.energia -= 5
                print("Świadkowie podają rysopis podejrzanego i opis samochodu, którym się poruszał.")
                print("Rozpoczynasz śledztwo mające na celu odnalezienie samochodu.")
            else:
                print("Decydujesz się nie przesłuchiwać świadków.")
        
        print("Zbierasz dalsze dowody na miejscu zbrodni.")
        print("Znajdujesz odciski palców i zabezpieczasz je do analizy.")
        self.policjant.energia -= 5
        if self.policjant.energia <= 0 or self.policjant.zdrowie <= 0:
            print("Niestety, nie masz już energii lub zdrowia. Gra skończona.")
            return
        
        print("Po kilku godzinach otrzymujesz wyniki analizy odcisków palców.")
        self.policjant.energia -= 5
        
        print("Wyniki analizy odcisków palców wskazują na konkretnego podejrzanego.")
        print("Czy chcesz przeprowadzić aresztowanie? (tak/nie): ")
        aresztowanie = input()
        if aresztowanie.lower() == 'tak':
            print("Zorganizowałeś zespół i przeprowadzasz aresztowanie podejrzanego.")
            print("Podejrzany zostaje zatrzymany i przewieziony na komisariat.")
            self.policjant.szczescie += 10
            self.policjant.energia -= 10
            self.policjant.zdrowie -= 5
        else:
            print("Decydujesz się nie przeprowadzać aresztowania na tym etapie.")
            self.policjant.szczescie -= 5
        
        print("Czas przesłuchać podejrzanego. Jak chcesz przeprowadzić przesłuchanie?")
        print("1. Twarde przesłuchanie")
        print("2. Łagodne podejście")
        print("3. Przesłuchanie z udziałem prawnika")
        wybor_przesluchania = input("Wybierz opcję (1/2/3): ")
        
        if wybor_przesluchania == '1':
            print("Przeprowadzasz twarde przesłuchanie.")
            self.policjant.szczescie -= 5
            self.policjant.zdrowie -= 5
            print("Podejrzany początkowo odmawia współpracy, ale po długim przesłuchaniu przyznaje się do winy.")
        elif wybor_przesluchania == '2':
            print("Stosujesz łagodne podejście.")
            self.policjant.szczescie += 5
            self.policjant.energia -= 5
            print("Podejrzany zaczyna współpracować i ujawnia ważne szczegóły dotyczące zbrodni.")
        elif wybor_przesluchania == '3':
            print("Przesłuchanie odbywa się z udziałem prawnika.")
            self.policjant.pieniadze -= 20
            print("Podejrzany korzysta z prawa do milczenia, ale prawnika udaje się przekonać do współpracy.")
            self.policjant.szczescie += 10
        else:
            print("Nie wybrano poprawnej opcji.")
        
        print("Śledztwo prowadzi cię do nowych dowodów, które mogą być kluczowe dla sprawy.")
        print("Odnajdujesz nowe miejsca związane ze zbrodnią:")
        print("1. Mieszkanie podejrzanego")
        print("2. Miejsce pracy podejrzanego")
        print("3. Ukryte miejsce spotkań gangu")
        wybor_miejsca = input("Gdzie chcesz się udać? (1/2/3): ")
        
        if wybor_miejsca == '1':
            print("Przeszukujesz mieszkanie podejrzanego i znajdujesz dowody, które potwierdzają jego udział w zbrodni.")
            print("Zabezpieczasz znalezione dowody i przesyłasz je do laboratorium.")
            self.policjant.energia -= 10
            self.policjant.szczescie += 10
        elif wybor_miejsca == '2':
            print("Odwiedzasz miejsce pracy podejrzanego i rozmawiasz z jego współpracownikami.")
            print("Zbierasz informacje, które potwierdzają alibi podejrzanego.")
            self.policjant.szczescie -= 10
        elif wybor_miejsca == '3':
            print("Odkrywasz ukryte miejsce spotkań gangu i znajdujesz dowody na zlecenie zbrodni przez lidera gangu.")
            print("Rozpoczynasz śledztwo przeciwko całemu gangowi.")
            self.policjant.szczescie += 15
            self.policjant.energia -= 15
        else:
            print("Nie wybrano poprawnej opcji.")
        
        print("Zbliżasz się do rozwiązania sprawy.")
        print("Czy chcesz zorganizować konferencję prasową, aby poinformować opinię publiczną o postępach śledztwa? (tak/nie): ")
        konferencja = input()
        if konferencja.lower() == 'tak':
            print("Organizujesz konferencję prasową i przedstawiasz najnowsze informacje na temat śledztwa.")
            print("Opinia publiczna jest zadowolona z twojej pracy.")
            self.policjant.szczescie += 20
        else:
            print("Decydujesz się nie organizować konferencji prasowej.")
            self.policjant.szczescie -= 5
        
        print("Otrzymujesz nowe informacje od tajnego informatora.")
        print("Informator przekazuje ci miejsce ukrycia dowodów.")
        print("Czy chcesz spotkać się z informatorem? (tak/nie): ")
        spotkanie_informator = input()
        if spotkanie_informator.lower() == 'tak':
            print("Spotykasz się z informatorem w wyznaczonym miejscu.")
            print("Informator przekazuje ci cenne dowody, które prowadzą do rozwiązania sprawy.")
            self.policjant.pieniadze -= 10
            self.policjant.energia -= 5
            self.policjant.szczescie += 15
        else:
            print("Decydujesz się nie spotykać z informatorem.")
            self.policjant.szczescie -= 5
        
        print("Kończysz śledztwo i przekazujesz sprawę do prokuratury.")
        print("Gratulacje! Rozwiązałeś sprawę morderstwa.")
        self.policjant.szczescie += 30

