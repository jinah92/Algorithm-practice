# 이상한 문자 만들기(level 1)
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    start_num = 0

    for word in range(0, len(s)):
        if s[word] == ' ':
            start_num = 0
            answer += ' '
        else:
            if start_num % 2 == 0:
                answer += s[word].upper()
            else:
                answer += s[word].lower()

            start_num += 1

    return answer