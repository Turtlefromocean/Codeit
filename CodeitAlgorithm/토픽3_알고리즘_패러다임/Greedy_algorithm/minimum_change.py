def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    count = 0
    result = value
    coin_list_sorted = sorted(coin_list, reverse=True)
    for i in range(0, len(coin_list_sorted)):
        while result >= coin_list_sorted[i]:
            result = result - coin_list_sorted[i]
            count = count + 1
    return count
# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))