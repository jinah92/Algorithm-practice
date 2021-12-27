def solution(absolutes, signs):
    return sum(list(map(lambda x, y: -y if x is False else y, signs, absolutes)))