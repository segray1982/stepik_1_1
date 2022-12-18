#!/usr/bin/env python3

print('Введите число для конвертации в десятичную систему:')
num = input().lower()
num_l = []
for char in num:
    if char == 'a':
        char = '10'
    if char == 'b':
        char = '11'
    if char == 'c':
        char = '12'
    if char == 'd':
        char = '13'
    if char == 'e':
        char = '14'
    if char == 'f':
        char = '15'
    num_l.append(char)

print('Введите кратность системы счисления:')
key = int(input())


result = 0
for i in range(len(num_l)):
    temp = int(num_l[i]) * (key ** (len(num_l) - i - 1))
    result += temp
print(result)