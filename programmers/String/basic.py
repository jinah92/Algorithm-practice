# level 1
# 문자열 다루기 기본
# url : https://programmers.co.kr/learn/courses/30/lessons/12918

s = 'a234'

def solution(s):

    answer = False

    if len(s) in (4, 6) and s.isdigit():
        answer = True

    return answer

print(solution(s))

