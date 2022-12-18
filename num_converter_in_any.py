#!/usr/bin/env python3
print('Введите число в десятичной системе для конвертации')
num = int(input())
print('Введите разрядность новой системы счисления')
key = int(input())
result = []
new = []
while num > 1:
    temp = num % key
    num = num // key
    new.append(temp)
new.append(num)
print(new)
for char in new:
    if char == 10:
        char = 'A'

    elif char == 11:
        char = 'B'

    elif char == 12:
        char = 'C'

    elif char == 13:
        char = 'D'

    elif char == 14:
        char = 'E'

    elif char == 15:
        char = 'F'
    result.append(char)
if result[-1] == 0:
    del result[-1]
print(result)
print(*result[::-1], sep='')


