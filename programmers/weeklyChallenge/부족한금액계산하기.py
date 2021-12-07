from functools import reduce

def solution(price, money, count):
    return max(reduce(lambda x,y : x + price * y, range(count+1)) - money, 0) 

solution(3, 20, 4)    