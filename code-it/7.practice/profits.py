# 특정 기간 중, 가장 수익이 많은 구간에서의 총 수익을 리턴하는 함수
def sublist_max(profits):
    profits_cases = []
    itr = len(profits)

    while(itr >0):
        idx = 0
        for i in range(idx, len(profits)):
            if (idx+itr) <= len(profits):
                profits_cases.append(sum(profits[i:itr+idx]))
            else:
                break
            idx += 1
        itr -= 1

    return max(profits_cases)



# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
