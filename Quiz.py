import random
from time import sleep

question = [
    ('Jaki jest wynik działania 2+2',['a) 1','b) 2','c) 3','d) 4'], 3),
    ('Który język używamy do tworzenia stron WWW', ['a) Python','b) HTML','c) Java', 'd) SQL'], 1),
    ('Ile nóg ma ma pająk', ['a) 8','b) 10', 'c) 12','d) 14'], 0),
    ('Który kolor powstaje po zmieszaniu niebieskiego i zółtego', ['a) Pomarańczowy','b) Fioletowy','c) Zielony','d) Czerwony'], 2),
    ('Co oznacza skrót SQL', ['a) Simple Question Language', 'b) Structured Query Language', 'c) Strong Quick Logic','d) System Quality List'], 1),
]
count = ('pierwsze', 'drugie', 'trzecie', 'czwarte', 'piąte')

def quiz():
    questions_left = 5
    punkts = 0
    count_count = 0

    while questions_left > 0:
        quest = random.choice(question)
        question.remove(quest)
        ask, choice, answer = quest

        answer_map = {
            'a' : 0,
            'b' : 1,
            'c' : 2,
            'd' : 3,
        }

        print(f'Losujemy {count[count_count]} pytanie: \n')
        sleep(2)
        print(ask,'\n', choice)
        player_choice = input('Jaka jest Twoja odpopwiedz? \n A,B,C,D?').lower()
        sleep(1)

        if answer_map[player_choice] == answer:
            questions_left -= 1
            punkts += 1
            count_count += 1
            print(f'Jest to poprawna odpowiedz \n\nZostały jeszcze {questions_left} pytania \nZdobyłeś kolejny punkt !!!__{punkts}__!!! :) ')
            print()
            sleep(2)
        else:
            questions_left -= 1
            count_count += 1
            print(f'Niestety jest to niepoprawna odpowiedz \n\nZostały jeszcze {questions_left} pytania \nNie zdobyłeś punktu :(')
            print()
            sleep(2)
while True:

    start = input('Witam w quizie, aby wygrać musisz poprawnie odpowiedzieć na przynajmniej 3 z 5 pytań.Czy jesteś gotowy na zabawę\n TAK/NIE').lower()

    if start == 'TAK'.lower():
        quiz()
        break
    elif start == 'NIE'.lower():
        print('Do zobaczenia :)')
        exit()
    else:
        print('Wybierz Tak lub Nie')



