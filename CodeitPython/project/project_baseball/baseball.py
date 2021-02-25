from random import randint


def generate_numbers():
    numbers = []
    # 코드를 작성하세요.

    count = 0

    while count < 3:
        random_number = randint(0, 9)
        if random_number not in numbers:
            numbers.append(random_number)
            count += 1

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    count = 0

    while count < 3:
        guess_number = int(input(f'{count + 1}번째 숫자를 입력하세요:'))
        if (guess_number > 9) or (guess_number < 0):
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
        elif guess_number not in new_guess:
            new_guess.append(guess_number)
            count += 1
        else:
            print('중복되는 숫자입니다. 다시 입력하세요.')

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(0, 3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.
while True:
    tries += 1
    my_guess = take_guess()
    score_s, score_b = get_score(my_guess, ANSWER)
    print(f'{score_s}S {score_b}B')
    if score_s == 3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))