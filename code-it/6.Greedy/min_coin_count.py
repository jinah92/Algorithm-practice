# 최소 동전으로 돈을 거슬러 주는 알고리즘
# value: 거슬러 줘야 하는 총액
# coin_list: 동전 리스트
# 거슬러 주기 위해 필요한 최소 동전 개수를 리턴

def min_coin_count(value, coin_list):
    coins = sorted(coin_list, reverse=True)
    count = 0
    
    for coin in coins:
        while(value % coin < value):
            add = value // coin
            count += add
            value = value % coin
    
    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
