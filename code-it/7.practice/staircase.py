# 출근하는 방법1
# 1계단 또는 2계단씩 오를 수 있을때, n개의 계단을 올라갈 수 있는 경우의 수를 리턴
cache = {}

def staircase(n):
    if n < 2:
        return 1
    if n in cache:
        return cache[n]
    
    cache[n] = staircase(n-1) + staircase(n-2)
    return cache[n]


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
