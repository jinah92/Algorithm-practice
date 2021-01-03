# level 1
# 문자열 내 마음대로 정렬하기

# URL: https://programmers.co.kr/learn/courses/30/lessons/12915


import numpy as np
from collections import Counter

strings = ['abce', 'abcd', 'cdx']
n = 2

def solution(strings, n):
    string_count = len(strings)
    answer = []
    for i in range(0, string_count):
        answer.append(strings[i])
    answer.sort(key = lambda str : (str[n],str));
    return answer


print(solution(strings, n))
