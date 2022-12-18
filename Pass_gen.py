#!/usr/bin/env python3
import random
digits = '0123456789'
low_alph = 'abcdefghijklmnopqrstuvwxyz'
up_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
bad_chars = 'il1Lo0O'
chars = digits
# Запросы
pass_quantity = int(input('Сколько паролей вам нужно?(цифра)     '))
lenth = int(input('Длина пароля?(цифра)     '))
need_up_alph = input('Включать ли прописные буквы?("+" - да/любая другая клавиша - нет)     ')
need_low_alph = input('Включать ли строчные буквы?("+" - да/любая другая клавиша - нет)     ')
need_punctuation = input(f'Включать ли символы: {punctuation}?("+" - да/любая другая клавиша - нет)     ')
except_bad_chars = input(f'Исключать ли {bad_chars}?("+" - да/любая другая клавиша - нет)     ')

if need_up_alph == '+'.lower().strip():
    chars += up_alph

if need_low_alph == '+'.lower().strip():
    chars += low_alph

if need_punctuation == '+'.lower().strip():
    chars += punctuation

if except_bad_chars == '+'.lower().strip():
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

print('Пользуйтесь:')

def is_password(lenth, chars):
    pass_list = []
    for i in range(lenth):
        password = random.choice(chars)
        pass_list.append(password)
    print(*pass_list, sep='')

while pass_quantity != 0:
    pass_quantity -= 1
    is_password(lenth, chars)