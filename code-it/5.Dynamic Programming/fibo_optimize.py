# tabulation방식
# 공간복잡도 O(1)로 기존의 피보나치 수열을 최적화
def fib_optimized(n):
    for val in range(0, n):
        if val == 0:
            current, previous = 1, 0
            continue
        tmp = current
        current = previous + current
        previous = tmp
    
    return current

# 테스트
print(fib_optimized(2))
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))