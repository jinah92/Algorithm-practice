# 특정 기간 중, 가장 수익이 많은 구간에서의 총 수익을 리턴하는 함수
#  divide and concquer
def sublist_max(profits, start, end):
    if start == end:
        return profits[start]

    mid = (start+end)//2

    left_sum = sublist_max(profits, start, mid)
    right_sum = sublist_max(profits, mid+1, end)
    mid_sum = max_crossing_site(profits, start, end)

    return max(left_sum, right_sum, mid_sum)


def max_crossing_site(profits, start, end):
    mid = (start + end)//2

    left_sum = 0    # 왼쪽 누적 수익
    left_max = profits[mid]  # 왼쪽 최고 수익

    for i in range(mid, start-1, -1):
        left_sum += profits[i]
        left_max = max(left_sum, left_max)

    right_sum = 0   # 오른쪽 누적 수익
    right_max = profits[mid+1]  # 오른쪽 최고 수익

    for i in range(mid+1, end+1):
        right_sum += profits[i]
        right_max = max(right_sum, right_max)

    return left_max + right_max


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9,
         2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))
