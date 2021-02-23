# tabulation
# 가능한 최대 수익(profit)을 리턴하는 함수
# price_list: 개수별 가격이 정리되어 있는 리스트
# count: 판매할 새꼼달꼼 개수

def max_profit(price_list, count):
    cache = {}
    cache[0], cache[1] = price_list[0], price_list[1]

    for i in range(1, count):
        sub_count = i+1
        profit = price_list[sub_count] if sub_count < len(price_list) else 0
        for j in range(1, sub_count//2 + 1):
            profit = max(profit, cache[j] + cache[sub_count-j])

        cache[sub_count] = profit

    return cache[count]

# 테스트
# print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
