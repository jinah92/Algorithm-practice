# 자연수 뒤집어 배열로 만들기 (레벨 1)
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    list_n = list(map(int, list(str(n))))
    list_n.reverse()
    return list_n

solution(12345)