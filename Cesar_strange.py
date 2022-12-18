#!/usr/bin/env python3
alph = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input()
temp_list = text.split(' ')
key_l = []
text_l = []
for char in temp_list:
    word = ''
    for c in char:
        if c in alph:
            word += c
    key = len(word)
    key_l.append(key)
for i in range(len(temp_list)):
    for c in temp_list[i]:
        if c not in alph:
            code = c
            text_l.append(code)
        elif c in alph:
            code = alph[alph.find(c) + key_l[i]]
            text_l.append(code)
    text_l.append(' ')
text_l[-1] = text_l[-1].rstrip()
print(*text_l, sep='')