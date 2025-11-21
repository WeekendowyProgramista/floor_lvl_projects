while True:

    while True:
        try:
            number1 = int(input("Podaj pierwszą cyfrę:"))
            break
        except ValueError:
            print("To nie jest cyfra! Spróbuj jeszcze raz ")
    while True:
        try:
            number2 = int(input("Podaj drugą cyfrę:"))
            break
        except ValueError:
            print("To nie jest cyfra! Spróbuj jeszcze raz ")


    print("Czego potrzebujesz?")
    print("a = dodawanie")
    print("b = odejmowanie")
    print("c = mnożenie")
    print("d = dzielenie")

    choice = input()

    while choice not in ["a", "b", "c", "d"]:

        print("Nie poprawny wybór, spróbuj jeszcze raz")
        print("___")
        print("a = dodawanie")
        print("b = odejmowanie")
        print("c = mnożenie")
        print("d = dzielenie")
        print("___")
        print("Czego potrzebujesz?")

        choice = input()

    if choice == "a":
        print(f"Twój wynik to:", (number1 + number2))
    elif choice == "b":
        print(f"Twój wynik to:", (number1 - number2))
    elif choice == "c":
        print(f"Twój wynik to:", (number1 * number2))
    elif choice == "d":
        if number2 == 0:
            print("Pamiętaj cholero nie dziel przez 0 :)")
            continue
        wynik = number1 / number2
        print("Twój wynik to:", wynik)
    else:
        print("Wybierz odpowiednią metodę")

    while True:
        kontynuuj = input("Czy chcesz kontynuować?(tak/nie)").lower()
        if kontynuuj == "tak":
            break
        elif kontynuuj == "nie":
            print("Dzięki za zabawę")
            exit()
        else:
            print("Nie rozumiem, wybierz tak lub nie")