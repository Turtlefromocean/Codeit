# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day + 1))

print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성", "유재석", "빌 게이츠"))
# format() 인덱스에 있는 값이 들가서 출력

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2: .2f}입니다.".format(num_1, num_2, num_1/num_2))
# 결과 값을 결과 float 값을 소수점 둘째자리까지 반올림하라
