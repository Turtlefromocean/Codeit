from random import randint


def generate_numbers(n):
    # 코드를 작성하세요.
    my_list = []
    count = 0
    while count < n:
        random_number = randint(1, 45)
        if random_number not in my_list:
            my_list.append(random_number)
            count += 1

    return my_list


def draw_winning_numbers():
    # 코드를 작성하세요.
    winning_numbers_list = []
    count = 0
    while count < 6:
        random_number = randint(1, 45)
        if random_number not in winning_numbers_list:
            winning_numbers_list.append(random_number)
            count += 1

    bonus_random_number = randint(1, 45)
    if bonus_random_number not in winning_numbers_list:
        winning_numbers_list.sort()
        winning_numbers_list.append(bonus_random_number)

    return winning_numbers_list


def count_matching_numbers(numbers, winning_numbers):
    # 코드를 작성하세요.
    count = 0
    for i in range(len(winning_numbers)):
        target = winning_numbers[i]
        if target in numbers:
            count += 1

    return count


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    general_numbers = winning_numbers[:6]
    bonus_number = winning_numbers[len(winning_numbers) - 1]

    general_count = 0
    bonus_count = 0

    for i in range(len(general_numbers)):
        target = general_numbers[i]
        if target in numbers:
            general_count += 1

    if bonus_number in numbers:
        bonus_count = 1

    if general_count == 6:
        return 1000000000
    elif general_count == 5 and bonus_count == 1:
        return 50000000
    elif general_count == 5:
        return 1000000
    elif general_count == 4:
        return 50000
    elif general_count == 3:
        return 5000

    return 0


# 테스트


# generate_numbers(6)
# print(draw_winning_numbers())
# numbers_test = [2, 4, 11, 14, 25, 40]
# winning_numbers_test = [2, 4, 10, 11, 14, 40, 25]
#
# print(check(numbers_test, winning_numbers_test))