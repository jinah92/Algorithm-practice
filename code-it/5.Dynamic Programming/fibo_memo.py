# 피보나치 수열을 memoization으로 구현

def fib_memo(n, cache):
    # 코드를 작성하세요.
    if cache[n] == 1 or cache[n] == 2:
        return 1
    
    return cache[n-2] + cache[n-1]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    for idx in range(1, n+1):
        if idx == 1 or idx == 2:
            fib_cache[idx] = 1
            continue
        fib_cache[idx] = fib_cache[idx-2]+fib_cache[idx-1]

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))