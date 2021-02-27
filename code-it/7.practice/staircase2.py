# 출근하는 방법1
# possible_steps의 방법으로 계단을 오를 수 있는 방법의 수를 리턴 (possible_steps는 항상 1을 포함한다)
def staircase(stairs, possible_steps):
    # 계단 높이가 0 또는 1일 때, 올라가는 방법은 1가지
    number_of_ways = [1, 1]

    for height in range(2, stairs+1):
        number_of_ways.append(0)

        for step in possible_steps:
            if height-step >= 0:
                number_of_ways[height] += number_of_ways[height-step]

    return number_of_ways[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
