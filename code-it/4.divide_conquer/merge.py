# 합병정렬 알고리즘
def merge(list1, list2):
    if len(list1) <= 1 and len(list2) <= 1:
        return sorted(list1+list2)

    return sorted(merge(list1[:len(list1)//2], list1[len(list1)//2:]) + merge(list2[:len(list2)//2], list2[len(list2)//2:]))      

# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
