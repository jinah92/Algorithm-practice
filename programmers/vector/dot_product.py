# 내적 (level 1)
# url: https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    n = len(a)

    for i in range(0, n):
        answer += a[i] * b[i]

    return answer