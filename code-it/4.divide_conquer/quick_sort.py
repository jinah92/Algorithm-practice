# quicksort는 파라미터로 리스트 하나와 리스트 내에서 정렬시킬 범위를 나타내는 인덱스 start와 인덱스 end를 받음
# 정렬된 새로운 리스트 반환이 아닌, 파라미터로 받는 리스트 자체를 정렬시키는 것

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    tmp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = tmp

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    p_idx = end
    p_val = my_list[end]   # pivot
    i, b = start, start # i: 현재 비교하는 인덱스 , b: pivot보다 큰 그룹의 첫번째 인덱스

    while i < p_idx:
        if my_list[i] <= p_val:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p_idx)

    return b

# 퀵 정렬
def quicksort(my_list, start, end):
    # base case
    if end - start < 1:
        return

    p_idx = partition(my_list, start, end)

    quicksort(my_list, start, p_idx-1)
    quicksort(my_list, p_idx+1, end)
    


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)
