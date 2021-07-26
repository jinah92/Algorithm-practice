# 수 찾기 : 1920
N = int(input())
A = {}.fromkeys(map(int, input().split(' ')), 1)
M = int(input())
check_nums = list(map(int, input().split(' ')))

for num in check_nums:
    if A.get(num):
        print(1)
    else:
        print(0)