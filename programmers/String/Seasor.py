# level 1
# 시저 암호
# url : https://programmers.co.kr/learn/courses/30/lessons/12926

s = 'a B z'
n = 4

def check_range(n, start, end=0):
    return start <= n <= end if end >=start else end <= n <= start

def f(x, increment): 
    if x == 32:
        return ' '
    if check_range(x, 65, 90):
        return chr(64 + (x+increment)%90) if (x+increment > 90) else chr(x+increment)
    if check_range(x, 97, 122):
        return chr(96 + (x+increment)%122) if (x+increment > 122) else chr(x+increment)

def solution(s, n):
    result = ""
    for i in s:
        result += f(ord(i), n)
    
    return result

print(solution(s, n))