def consecutive_sum(start, end):
    if start == end:    # base case
        return start 
    
    return consecutive_sum(start, (start+end)//2) + consecutive_sum((start+end)//2 + 1, end)


    # 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
