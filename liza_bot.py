# Города
import random

goroda = ['Астрахань', 'Мурманск', 'Ярославль', 'Рыбинск', 'Архангельск',
          'Пикалево', 'Череповец', 'Кострома', 'Москва', 'Петропавловск-Камчатский',
          'Йошкар-Ола', 'Тула', 'Сочи', 'Мончегорск', 'Северодвинск', 'Пермь',
          'Глазов', 'Владимир', 'Екатеринбург', 'Челябинск', 'Омск', 'Новгород'
          ]


def proverka(gorod):  # посылается постоянно ng - исправить
    print(goroda)
    # if v != gorod[0]:
    #     return -1
    v = gorod[-1].upper()  # последний символ введенного города и преобразование в большую
    for s in goroda:
        if v == s[0]:  # прошли по списку и сравнили последнюю букву с первой буквой городов из списка goroda
            global gd
            gd = s
            goroda.remove(s)
            break
        elif v in ['Ъ', 'Ь', 'Ы', 'Ё']:
            v = gorod[-2].upper()
    return gd


def start(world):
    # while True:
    #     gorod = world.title()
    #     #gorod = input('Введите город\n').title()
    #     # try:
    #     if proverka(gorod, v) == -1:
    #         print('Город введен неправильно')
    #         continue
    #     goroda.remove(gorod)
    print('Привет! Добро пожаловать в игру "Города"')
    ng = random.choice(goroda)  # в переменной случайный город из списка goroda
    goroda.remove(ng)  # удалить првый случайный город ng из списка goroda
    v = ng[-1].upper()  # вытаскиваем последнюю букву из случайного города
    print("Начали")
    print(goroda)
    return 'Привет! Добро пожаловать в игру "Города"\n Я начинаю играть, мой город: '+ ng + '\n Теперь твой город?'

    # gorod = world.title()
    # # gorod = input('Введите город\n').title()
    # # try:
    # if proverka(gorod, v) == -1:
    #     print('Город введен неправильно')
    #goroda.remove(gorod)

    # start(1)

