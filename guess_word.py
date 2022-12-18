#!/usr/bin/env python3
import random
word_list = ['математика', 'физика', 'химия', 'биология', 'генетика', 'кибернетика', 'философия', 'анатомия']
def get_word(): # Случайное слово
    word = random.choice(word_list)
    return word
def is_stage_0(): # Висилица
    result = '''У вас есть 6 попыток до повешения
       --------
       |      |
       |
       |
       |
       |
       -'''
    return result
def is_stage_1(): # Висилица
    result = '''У вас еще есть 5 попыток до повешения
       --------
       |      |
       |      0
       |
       |
       |
       -'''
    return result
def is_stage_2(): # Висилица
    result = '''У вас пока есть 4 попытки до повешения
       --------
       |      |
       |      0
       |      |
       |      |
       |
       -'''
    return result
def is_stage_3(): # Висилица
    result = '''У вас есть всего 3 попытки до повешения
       --------
       |      |
       |      0
       |     \\|/
       |      |
       |
       -'''
    return result
def is_stage_4(): # Висилица
    result = '''У вас осталось 2 попытки до повешения
       --------
       |      |
       |      0
       |     \\|/
       |      |
       |     /
       -'''
    return result
def is_stage_5(): # Висилица
    result = '''У вас осталась ПОСЛЕДНЯЯ попытка!!!
       --------
       |      |
       |      0
       |     \\|/
       |      |
       |     / \\
       -'''
    return result
def is_stage_6(): # Висилица
    result = '''
       --------
       |      |
       |      0
       |      |
       |     /|\\
       |     / \\
       -
      G A M E  O V E R'''
    return result
def display_hangman(tries): # Вывод нужной висилицы
    if tries == 6:
        print(is_stage_0())
    elif tries == 5:
        print(is_stage_1())
    elif tries == 4:
        print(is_stage_2())
    elif tries == 3:
        print(is_stage_3())
    elif tries == 2:
        print(is_stage_4())
    elif tries == 1:
        print(is_stage_5())
    elif tries == 0:
        print(is_stage_6())
def play(): # Старт
    guessed_letters = []  # список уже названных букв
    print('''Привет. Давайте поиграем в виселицу. Я загадал слово. Тема: "Название науки". 
Вам нужно угадать его. У вас есть шесть возможностей ошибиться. 
Вы называете букву, если ее нет в слове, то - минус одна попытка.''')
    print('Приступим. Вот загаданное слово:')
    word = get_word()
    word = word.upper()
    completion = '_ ' * len(word) # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = completion.split()
    print(*word_completion)
    print()
    tries = 6
    display_hangman(tries)
    flag = False
    while flag == False:
        print('Назовите букву:')
        letter = input().upper()
        if letter in guessed_letters:
            print('Вы уже называли эту букву.')
            flag = False
        elif not letter.isalpha():
            print('Внимательнее!')
            flag = False
        else:
            flag = True
    guessed_letters.append(letter)
    print('Буквы, которые вы уже называли: ', end='')
    print(*guessed_letters)
    while tries >= 0:
        if letter.upper() not in word.upper():
            print('Не угадали.')
            tries -= 1
            if tries == 0:
                print(f'Вы проиграли!!! Это было слово {word}.')
                print()
                print(f'Если хотите сыграть еще, нажмите 1, если нет - нажмите любую другую клавишу.')
                choice = input()
                if choice == '1':
                    play()
                else:
                    exit()
            display_hangman(tries)
            print(*word_completion)
            flag = False
            while flag == False:
                print('Назовите букву:')
                letter = input().upper()
                if letter in guessed_letters:
                    print('Вы уже называли эту букву.')
                    flag = False
                elif not letter.isalpha():
                    print('Внимательнее!')
                    flag = False
                else:
                    flag = True
            guessed_letters.append(letter)
            print('Буквы, которые вы уже называли: ', end='')
            print(*guessed_letters)
        elif letter.upper() in word.upper():
            print('Есть такая буква в этом слове.')
            for i in range(len(word)):
                if word[i] == letter:
                    word_completion[i] = letter
            if '_' not in word_completion:
                print()
                print(f'Правильно, {word}!!!')
                print()
                print('Поздравляем. Вы победили!!!')
                print()
                print('Если хотите сыграть еще, нажмите 1, если нет - нажмите любую другую клавишу.')
                choice = input()
                if choice == '1':
                    play()
                else:
                    exit()
            print()
            print(*word_completion)
            print()
            print('Давайте угадывать следующую букву.')
            display_hangman(tries)
            flag = False
            while flag == False:
                print('Назовите букву:')
                letter = input().upper()
                if letter in guessed_letters:
                    print('Вы уже называли эту букву.')
                    flag = False
                elif not letter.isalpha():
                    print('Внимательнее!')
                    flag = False
                else:
                    flag = True
            guessed_letters.append(letter)
            print('Буквы, которые вы уже называли: ', end='')
            print(*guessed_letters)
play()