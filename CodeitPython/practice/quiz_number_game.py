import random

answer = random.randint(1, 20)
# 코드를 작성하세요.
chance = 4

while chance >= 0:
    if chance == 0:
        print(f'아쉽습니다. 정답은 {answer}였습니다')
        break

    my_answer = int(input(f"기회가 {chance}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if my_answer == answer:
        print(f'축하합니다. {4 - chance + 1}번만에 숫자를 맞히셨습니다.')
        break
    elif my_answer > answer:
        print('Down')
    else:
        print('Up')

    chance -= 1
