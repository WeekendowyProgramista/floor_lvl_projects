import random
import time

print('Gra w Papier, Kamien, Nozyce. Pokonaj komputer w walce na 4 rundy.')
gra = ('kamień', 'papier', 'nożyce')

licznik = 4
wygrana = 0
przegrana = 0

time.sleep(2)

for i in range(licznik):
    while True:
        wybor_gracz = input(str('Twój wybór:'))
        wybor_komputer = random.choice(gra)

        if wybor_gracz not in gra:
            print('Wybierz jedną z opcji! papier, kamień, nożyce')
        else:
            print(f'Komputer wybrał: {wybor_komputer}')
            break

    time.sleep(1)

    if wybor_gracz == wybor_komputer:
        licznik = licznik - 1
        print(f'Remis!!!\nNikt nie otrzymuje punktu.\nIlość gier: {licznik}')
    elif wybor_gracz == 'kamień' and wybor_komputer == 'nożyce'or\
        wybor_gracz == 'papier' and wybor_komputer == 'kamień' or\
        wybor_gracz == 'nożyce' and wybor_komputer == 'papier':
        wygrana = wygrana + 1
        licznik = licznik - 1
        print('Wygrałeś!!!')
        print(f'Otrzymujesz {wygrana} punkt')
        print(f'Ilość gier: {licznik}')
    else:
        przegrana = przegrana + 1
        licznik = licznik - 1
        print('Przegrałeś!!!')
        print(f'Komputer otrzymuje {przegrana} punkt')
        print(f'Ilość gier: {licznik}')

    if licznik == 1:
        print('Ostatnia runda!')
    elif licznik == 0:
        print('Koniec gry!')

time.sleep(1)
print('Zliczanie głosów...')
time.sleep(1)

if wygrana > przegrana:
    print(f'Grę wygał gracz z wynikiem {wygrana} do {przegrana}\n!!!GRATULACJE!!!')
elif wygrana < przegrana:
    print(f'Grę wygrał komputer z wynikiem {przegrana} do {wygrana}')
else:
    print('Nastąpił remis!')


