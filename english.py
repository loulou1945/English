questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']

counter = len(questions)
counter_answer = 0
points = 0

print("Привет! Предлагаю проверить свои знания английского!")
print('Напиши, как тебя зовут.')

name = input()
print(f'Привет, {name}! Наберите "ready", чтобы начать')

answer = input()

if answer == 'ready':
    for number in range(len(questions)):
        counter_attempts = 2
        print(questions[number])
        answer = input()
        while counter_attempts != 0:
            if answer == answers[number]:
                counter_answer += 1
                points = points + counter_attempts + 1
                print('Ответ верный!!')
                print(f'Вы получаете {counter_attempts + 1} баллa!')
                break
            else:
                print('Неправильно')
                print(f'Осталось попыток: {counter_attempts}, попробуйте еще раз!')
                answer = input()
            counter_attempts -= 1
        if counter_attempts == 0:
            print(f'Увы, но нет. Правильный ответ: {answers[number]}')
        print()

    print(f'Вот и все, {name}!')
    print(f'Вы ответили на {counter_answer} вопросов из {counter} верно.')
    print(f'Вы заработали {points} баллов')

    percent = int(counter_answer / counter* 100)
    print(f'Это {percent} процентов')
else:
    print('Кажется вы не хотите играть. Очень жаль.')


