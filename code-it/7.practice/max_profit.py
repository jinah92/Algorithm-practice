# 삼송전자 주식을 딱 한번만 사고 팔 때, 최대 수익
# 시간복잡도 : O(n)
def max_profit(stock_list):
    #  현재까지 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 현재까지의 최소 주식가격
    min_value = min(stock_list[0], stock_list[1])

    for i in range(2, len(stock_list)):
        # 현재 파는것이 좋은지 확인
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_value)
        # 현재 주식값이 최솟값인지 확인
        min_value = min(min_value, stock_list[i])

    return max_profit_so_far



# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))