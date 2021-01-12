# 정수 내림차순으로 배치하기(level 1)
# url : https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    str_list = list(str(n))
    updated_list = [int(x) for x in str_list]

    for i in range(0, len(updated_list)-1):
        max, idx = updated_list[i], i
        for j in range(i+1, len(updated_list)):
            if max < updated_list[j]:
                max = updated_list[j]
                idx = j
        
        if updated_list[i] < max:
            tmp = updated_list[i]
            updated_list[i] = updated_list[idx]
            updated_list[idx] = tmp

    return int(''.join([str(x) for x in updated_list]))

print(solution(118372))