# 강남역 폭우
# 기존 brute force방법보다, 공간을 좀 더 써서 시간복잡도를 줄이는 방법
def trapping_rain(buildings):
    total_height = 0
    left_list, right_list = [0]*len(buildings), [0]*len(buildings)
    left_list[0], right_list[-1] = buildings[0], buildings[-1]

    # left[i], right[i]: i번째 빌딩을 기준으로 왼쪽, 오른쪽에서 가장 높은 빌딩의 높이를 저장
    for i in range(1, len(buildings)-1):
        left_list[i] = max(left_list[i-1], buildings[i])
    
    for i in range(len(buildings)-2, -1, -1):
        right_list[i] = max(right_list[i+1], buildings[i])
    
    for i in range(len(buildings)):
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(left_list[i], right_list[i])
        # upper_bound가 현재 빌딩 높이보다 작은 경우, 담길 수 있는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])
    
    return total_height

    
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))