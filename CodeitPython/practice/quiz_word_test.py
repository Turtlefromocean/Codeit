with open('vocabulary.txt', 'r') as f:
    for line in f:
        information = line.strip().split(': ')
        # print(information[0], information[1])
        question = information[1]
        answer = information[0]

        my_answer = input(f'{question}:')
        if my_answer == answer:
            print('맞았습니다!')
        else:
            print(f'아쉽습니다. 정답은 {answer}입니다.')
