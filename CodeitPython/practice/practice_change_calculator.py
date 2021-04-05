def calculate_change(payment, cost):
    # 코드를 작성하세요.
    change = payment - cost

    print("50000원 지폐: {}장".format(change//50000))
    change -= 50000 * (change//50000)

    print("10000원 지폐: {}장".format(change//10000))
    change -= 10000 * (change//10000)

    print("5000원 지폐: {}장".format(change//5000))
    change -= 5000 * (change//5000)

    print("1000원 지폐: {}장".format(change//1000))
    change -= 1000 * (change//1000)


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)


# 모범답
# def calculate_change(payment, cost):
#     change = payment - cost  # 거스름돈 총액
#
#     fifty_count = change // 50000  # 50,000원 지폐
#     ten_count = (change % 50000) // 10000  # 10,000원 지폐
#     five_count = (change % 10000) // 5000  # 5,000원 지폐
#     one_count = (change % 5000) // 1000  # 1,000원 지폐
#
#     # 답 출력안
#     print("50000원 지폐: {}장".format(fifty_count))
#     print("10000원 지폐: {}장".format(ten_count))
#     print("5000원 지폐: {}장".format(five_count))
#     print("1000원 지폐: {}장".format(one_count))
