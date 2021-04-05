def min_fee(pages_to_print):
    # 코드를 작성하세요.
    minimum_fee = 0
    pages_sorted = sorted(pages_to_print)
    for i in range(0, len(pages_sorted)):
        minimum_fee = minimum_fee + pages_sorted[i] * (len(pages_sorted) - i)

    return minimum_fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
