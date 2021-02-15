# pivot 기준으로 재배치 후, pivot의 최종 위치 인덱스를 반환
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    tmp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = tmp

    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    p = my_list[end]   # pivot
    i, b = start, start

    for target in my_list:
        if target > p:
            i += 1
        elif target < p:
            my_list = swap_elements(my_list, i, b)
            b += 1
            i += 1    

    my_list = swap_elements(my_list, end, b)

    return my_list.index(p)

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
