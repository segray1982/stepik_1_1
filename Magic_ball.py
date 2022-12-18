#!/usr/bin/env python3
import random
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', '	Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', '	Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', '	Перспективы не очень хорошие', 'Весьма сомнительно']
name = input('Привет. Как тебя зовут?    ')
intro = print(f'Привет, {name}, я магический шар, и я знаю ответ на любой твой вопрос.')

while True:
    question = input('Спрашивай:     ')
    choice = random.randrange(len(answers))
    print(random.choice(answers))
    again = input('Если хочешь ещё что-нибудь спросить, напиши "да" (или нажми любую клавишу для завершения):    ')
    if again != 'да':
        print('Пока. Возвращайся если возникнут вопросы')
        break