import random

information = []

with open('vocabulary.txt', 'r') as f:
    for line in f:
        info = line.strip()
        information.append(info)

    count = len(information) - 1

    while True:
        N = random.randint(0, count)
        question = information[N].split(': ')
        korean = question[1]
        answer = question[0]
        my_answer = input(f'{korean}:')
        if my_answer == 'q':
            break
        elif my_answer == answer:
            print('맞았습니다!')
        else:
            print(f'틀렸습니다. 정답은 {answer}입니다.')
