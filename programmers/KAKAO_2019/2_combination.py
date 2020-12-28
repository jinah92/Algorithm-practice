# level 1
# 두 개 뽑아서 더하기

# URL: https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer = []
    cases = list(combinations(numbers, 2))
    for case in cases:
        answer.append(case[0] + case[1])

    return sorted(list(set(answer)))