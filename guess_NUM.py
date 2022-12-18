#!/usr/bin/env python3

import random

while True:
    print('Приветствую. Давайте поиграем в числовую угадайку. Я загадаю число, а вы будете уго угадывать.')
    # Ввод диапазона и проверка
    def is_dip():
        while True:
            dip = input('Введите число, от 1 до которого мне можно загадывать число:     ')
            if dip.isnumeric():
                dip = int(dip)
                break
        return dip
    dip = is_dip()

    # Случайное число
    def is_rand():
        rand = random.randint(1, dip)
        return rand
    rand = is_rand()

    # Ввод числа и проверка
    def is_num():
        num = input(f'Введите число от 1 до {dip}:     ')
        if num.isnumeric():
            num = int(num)
            if num not in range(1, dip + 1):
                num = input(f'Внимательнее. Введите число от 1 до {dip}:     ')
            else:
                return num

    # Сравнение чисел
    def compare_num():
        if num > rand:
            print('Слишком много, попробуйте еще.')
            compare = False
        elif num < rand:
            print('Слишком мало, попробуйте еще.')
            compare = False
        elif num == rand:
            compare = True
        return compare

    # Старт
    print(f'Я загадал число от 1 до {dip}. Попробуйте угадать его.')
    count = 1
    num = is_num()
    compare = compare_num()

    while compare == False:
        count += 1
        num = is_num()
        compare = compare_num()
    if compare == True:
        print('Правильно!')
        print(f'Количество попыток: {count}.')
        print('Хотите сыграть ещё?')
        plus = input('Нажмите "+", если хотите сыграть ещё, или любую другую клавишу для завершения игры:     ')
        if plus != '+':
            print('GAME OVER')
            exit()


