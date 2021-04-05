def fib_tab(n):
    # 코드를 작성하세요.
    fib = {1: 1, 2: 1}
    if n > 2:
        for i in range(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))