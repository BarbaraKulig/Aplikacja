class OsobistyAsystent:
    def __init__(self):
        self.ksiazka_adresowa = {}
        self.notatki = []

    def dodaj_do_ksiazki_adresowej(self, imie, numer_telefonu):
        self.ksiazka_adresowa[imie] = numer_telefonu
        print(f"Dodano {imie} do książki adresowej.")

    def wyszukaj_w_ksiazce_adresowej(self, imie):
        if imie in self.ksiazka_adresowa:
            print(f"Numer telefonu dla {imie}: {self.ksiazka_adresowa[imie]}")
        else:
            print(f"{imie} nie istnieje w książce adresowej.")

    def dodaj_notatke(self, notatka):
        self.notatki.append(notatka)
        print("Dodano notatkę.")

    def wyswietl_notatki(self):
        if self.notatki:
            print("Twoje notatki:")
            for i, notatka in enumerate(self.notatki, 1):
                print(f"{i}. {notatka}")
        else:
            print("Nie masz żadnych notatek.")

if __name__ == "__main__":
    asystent = OsobistyAsystent()

    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj do książki adresowej")
        print("2. Wyszukaj w książce adresowej")
        print("3. Dodaj notatkę")
        print("4. Wyświetl notatki")
        print("5. Wyjdź")

        wybor = input("Wybierz numer opcji: ")

        if wybor == "1":
            imie = input("Podaj imię: ")
            numer_telefonu = input("Podaj numer telefonu: ")
            asystent.dodaj_do_ksiazki_adresowej(imie, numer_telefonu)
        elif wybor == "2":
            imie = input("Podaj imię do wyszukania: ")
            asystent.wyszukaj_w_ksiazce_adresowej(imie)
        elif wybor == "3":
            notatka = input("Dodaj notatkę: ")
            asystent.dodaj_notatke(notatka)
        elif wybor == "4":
            asystent.wyswietl_notatki()
        elif wybor == "5":
            print("Dziękuję za skorzystanie z Osobistego Asystenta.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
