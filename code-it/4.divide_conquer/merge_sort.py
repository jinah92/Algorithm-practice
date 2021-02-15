# Divide and Conquer 방식으로 합병정렬 구현
def merge(list1, list2):
    if len(list1) <= 1 and len(list2) <= 1:
        return sorted(list1+list2)

    return sorted(merge(list1[:len(list1)//2], list1[len(list1)//2:]) + merge(list2[:len(list2)//2], list2[len(list2)//2:]))

# 합병 정렬
def merge_sort(my_list):
    if my_list == sorted(my_list):
        return my_list
    
    return merge(my_list[:len(my_list)//2], my_list[len(my_list)//2:])

    # 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
