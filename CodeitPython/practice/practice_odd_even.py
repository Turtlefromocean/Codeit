def is_evenly_divisible(number):
    # 코드를 작성하세요
    if number % 2 == 0:
        return True
    else:
        return False

# 모범답안
# 그냥 return number % 2 == 0


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))