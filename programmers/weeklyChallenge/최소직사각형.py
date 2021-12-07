def solution(sizes):
    resorted_sizes = list(map(lambda x : [x[0], x[1]] if x[0] >= x[1] else [x[1], x[0]], sizes))
    return max(resorted_sizes, key=lambda x : x[0])[0] * max(resorted_sizes, key=lambda x : x[1])[1]


# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes))