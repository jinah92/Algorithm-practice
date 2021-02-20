# 피보나치 수열을 tabulation 방식으로 구현
def fib_tab(n):
    fib_table = [0, 1, 1]
    for idx in range(3, n+1):
        fib_table.append(fib_table[idx-2] + fib_table[idx-1])
    
    return fib_table[n]
            
    # 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
