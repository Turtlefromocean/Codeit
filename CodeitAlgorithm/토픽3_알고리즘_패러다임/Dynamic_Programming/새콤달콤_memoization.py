def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]

    if count in cache:  # cache.get(count) != None
        return cache[count]
    else:
        max_i = 0
        for i in range(1, (count // 2) + 1):
            max_i = max(max_i, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))

        cache[count] = max_i

        if count < len(price_list) - 1:
            cache[count] = max(cache[count], price_list[count])

        return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
