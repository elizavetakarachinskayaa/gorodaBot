#Города
import random
goroda = ['Астрахань', 'Мурманск', 'Ярославль', 'Рыбинск', 'Архангельск',
          'Пикалево', 'Череповец', 'Кострома', 'Москва', 'Петропавловск-Камчатский',
          'Йошкар-Ола', 'Тула', 'Сочи', 'Мончегорск', 'Северодвинск', 'Пермь',
          'Глазов', 'Владимир', 'Екатеринбург', 'Челябинск', 'Омск', 'Новгород'
          ]
print('Привет! Добро пожаловать в игру "Города"')
ng = random.choice(goroda) #в переменной случайный город из списка goroda
goroda.remove(ng) #удалить првый случайный город ng из списка goroda
v = ng[-1].upper() #вытаскиваем последнюю букву из случайного города
print(ng)
def proverka(gorod, v): #посылается постоянно ng - исправить
    if v != gorod[0]:
        return -1
    v = gorod[-1].upper()  # последний символ введенного города и преобразование в большую
    for s in goroda:
        if v == s[0]:  # прошли по списку и сравнили последнюю букву с первой буквой городов из списка goroda
            print(s)
            goroda.remove(s)
            break
        elif v in ['Ъ', 'Ь', 'Ы', 'Ё']:
            v = gorod[-2].upper()
while True:
    gorod = input('Введите город\n').title()
    #try:
    if proverka(gorod, v) == -1:
        print ('Город введен неправильно')
        continue
    goroda.remove(gorod)