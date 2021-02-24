# 전체 수업에서 가장 많은 수업을 들을 수 있는 수를 리턴
# (시작시간, 종료시간)

def course_selection(course_list):
    selected_course = []
    course_list.sort(key=lambda x: (x[1], x[0]))
    # 가장 먼저 끝나는 수업부터 고르기
    for course in course_list:
        if len(selected_course) == 0:
            selected_course.append(course)
            continue
        if course[0] > max(selected_course)[1]:
            selected_course.append(course)
    
    return selected_course
        
# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10),
                        (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
