# 가장 적은 수의 약수터를 들르는 방법
# 약수터를 들르는 위치의 리스트를 리턴
def select_stops(water_stops, capacity):
    stops = []
    idx, sum = 0, water_stops[0]

    while(idx < len(water_stops)):
        if idx > 0:
            sum += water_stops[idx] - water_stops[idx-1]

        if sum >= capacity:
            if sum == capacity:
                stops.append(water_stops[idx])
            else:
                stops.append(water_stops[idx-1])
                idx -= 1
            sum = 0 

        idx += 1
    
    if stops[-1] != water_stops[-1]:
        stops.append(water_stops[-1])

    return stops

# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
