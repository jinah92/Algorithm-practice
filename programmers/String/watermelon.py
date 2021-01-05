# level 1

# 수박수박수박수박수박수?
# url : https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    return  ('수박'*(n//2)) if (n%2)==0 else ('수박'*(n//2) + '수')

print(solution(3))