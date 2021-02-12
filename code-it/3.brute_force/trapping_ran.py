def trapping_rain(buildings):
    max_height = max(buildings) # 가장 높이가 큰 값
    total = 0 # 빗물 총계

    for i in range(1, len(buildings)-1):
        if buildings[i] == max_height:
            continue
        max_left, max_right = max_left_right(buildings[:i], buildings[i:])
        if max_left == 0 or max_right == 0 or buildings[i] > max_left or buildings[i] > max_right:
            continue
        total += min(max_left, max_right) - buildings[i]

    return total


def max_left_right(left, right):
    return max(left), max(right)

# 테스트
# print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
