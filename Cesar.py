#!/usr/bin/env python3

while True:
    # Шифрование или дешифровка
    def is_answer():
        print('Введите "1" для шифрования или "2" для дешифровки текста:')
        answer = input().strip()
        while answer not in '12':
            print('Внимательнее! Введите "1" для шифрования или "2" для дешивровки текста:')
            answer = input().strip()
        return answer

    # Шифрование
    def is_code():
        text_l = []
        for c in text:
            if c not in alph:
                code = c
                text_l.append(code)
            else:
                code = alph[alph.find(c) + key]
                text_l.append(code)
        return text_l

    # Дешифровка
    def is_uncode():
        text_l = []
        for c in text:
            if c not in alph:
                code = c
                text_l.append(code)
            else:
                uncode = alph[alph.rfind(c) - key]
                text_l.append(uncode)
        return text_l

    # Выбор языка
    def is_lang():
        print('Введите "1" для кирилицы или "2" для латиницы:')
        lang = input().strip()
        while lang not in '12':
            print('Внимательнее! Введите "1" для кирилицы или "2" для латиницы:')
            lang = input().strip()
        return lang

    us = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    answer = is_answer()
    lang = is_lang()
    if lang == '1':
        alph = ru
        print('Введите ключ - цифру от 1 до 32')
        key = int(input())
        while key not in range(1, 33):
            print('Внимательнее! Введите ключ - цифру от 1 до 32')
            key = int(input())
    elif lang == '2':
        alph = us
        print('Введите ключ - цифру от 1 до 26')
        key = int(input())
        while key not in range(1, 27):
            print('Внимательнее! Введите ключ - цифру от 1 до 26')
            key = int(input())

    print('Введите текст для обработки:')
    text = input()

    if answer == '1':
        code = is_code()
        print('Результат обработки:')
        print()
        print(*code, sep='')
        print()
    else:
        uncode = is_uncode()
        print('Результат обработки:')
        print()
        print(*uncode, sep='')
        print()

    print('Если хотите обработать следующий текст, нажмите "1" или любую другую клавишу для выхода:')
    ex = input()
    if ex != '1':
        exit()

