# URL: https://programmers.co.kr/learn/courses/30/lessons/64061

import numpy as np

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# result = 4
temp_arr = []
result_arr = []
cnt = 0

for move in moves:
    temp_arr = [i[move-1] for i in board]
    for i in range(0, len(temp_arr)):
        if temp_arr[i]:
            result_arr.append(temp_arr[i])
            board[i][move-1] = 0

            if len(result_arr) > 1:
                for i in range(0, len(result_arr)):
                    if i == len(result_arr)-1:
                        break
                    if result_arr[i] == result_arr[i+1]:
                        cnt += 2
                        del result_arr[i:i+2]
                        break
            break

print(cnt)