def course_selection(course_list):
    # 코드를 작성하세요.
    sorted_list = sorted(course_list, key=lambda x: x[1])
    class_list = []
    class_list.append(sorted_list[0])
    for idx, schedule in enumerate(sorted_list):

        if idx > 0:
            if schedule[0] > class_list[-1][1]:
                class_list.append((schedule[0], schedule[1]))

    return class_list


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
