# leve 1
# 3진법 뒤집기

# URL: https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    invert_num = ''
    
    while n > 0 :
        n, mod = divmod(n, 3)
        invert_num += str(mod)

    return int(str(invert_num), base = 3)