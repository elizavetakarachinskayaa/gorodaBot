# Города
import random, db

# goroda = ['Мурманск', 'Ярославль', 'Рыбинск', 'Архангельск',
#           'Пикалево', 'Череповец', 'Кострома', 'Москва', 'Петропавловск-Камчатский',
#           'Йошкар-Ола', 'Тула', 'Сочи', 'Мончегорск', 'Северодвинск', 'Пермь',
#           'Глазов', 'Владимир', 'Екатеринбург', 'Челябинск', 'Омск', 'Новгород', 'Кропоткин'
#           ]
q = "SELECT  town FROM siti"
goroda = db.query(q)
v = ''
def proverka(gorod):  # посылается постоянно ng - исправить
    #print(goroda)
    global goroda
    global v
    print('proverka', v)

    if v != gorod[0].lower():
        return -1
    city_exist = False
    if gorod.title() in goroda:
        goroda.remove(gorod)
        scroll_letters(gorod)
        return 0
    else:
        return -2




def scroll_letters(gorod):
    global goroda
    global v

    letter_exists = False
    unfound_letters = []
    i = 0

    for letter in gorod:

        letter_exists = False
        for city in goroda:

            if city[0].lower() == gorod[-1 - i].lower():  # Начинаем с последней буквы. Если на нее нет городов - предпоследняя и т.д. до начала

                letter_exists = True
                break

        if letter_exists:

            v = gorod[-1 - i].lower()
            print('scroll_letters', v)
            break

        unfound_letters.append(gorod[-1 - i])
        i += 1

    return unfound_letters
    # gd = ' город введен неправильно '
    # v = gorod[-1].upper()  # последний символ введенного города и преобразование в большую
    # print(v)
    # for s in goroda:
    #     if v == s[0]:  # прошли по списку и сравнили последнюю букву с первой буквой городов из списка goroda
    #
    #         gd = s
    #         goroda.remove(s)
    #         break
    #     elif v in ['Ъ', 'Ь', 'Ы', 'Ё']:
    #         v = gorod[-2].upper()
    # return gd
    # letter_exists = False

def bot_reply():
    global goroda
    global v
    reply_message = ''
    for city in goroda:
        if v == city[0].lower():
            goroda.remove(city)
            scroll_letters(city)
            reply_message = city
            break

    return reply_message


def start(world):
    global v
    print('Привет! Добро пожаловать в игру "Города"')
    ng = random.choice(goroda)  # в переменной случайный город из списка goroda
    goroda.remove(ng)  # удалить првый случайный город ng из списка goroda
    start_message = 'Привет! Добро пожаловать в игру "Города"\n Я начинаю играть, мой город: ' + ng + '\n'
    scroll_letters(ng)
    # for letter in unfound_letters:
    #
    #     start_message += "Городов на букву " + letter + " нет\n"


    start_message += "Назови город на букву " + v + '\n'
    print("Начали")
    print(goroda)
    return start_message
    # while True:
    #     gorod = world.title()
    #     #gorod = input('Введите город\n').title()
    #     # try:
    #     if proverka(gorod, v) == -1:
    #         print('Город введен неправильно')
    #         continue
    #     goroda.remove(gorod)
    # print('Привет! Добро пожаловать в игру "Города"')
    # ng = random.choice(goroda)  # в переменной случайный город из списка goroda
    # goroda.remove(ng)  # удалить первый случайный город ng из списка goroda
    # global v
    # v = ng[-1].lower()  # вытаскиваем последнюю букву из случайного города
    # print('start', v)
    # print("Начали")
    # print(goroda)
    # return 'Привет! Добро пожаловать в игру "Города"\n Я начинаю играть, мой город: '+ ng + '\n Теперь твой город?'

    # gorod = world.title()
    # # gorod = input('Введите город\n').title()
    # # try:
    # if proverka(gorod, v) == -1:
    #     print('Город введен неправильно')
    # goroda.remove(gorod)

    # start(1)
