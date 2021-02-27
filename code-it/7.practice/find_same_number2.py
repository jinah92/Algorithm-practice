# 중복된 수를 리턴하는 함수  (non-brute force)
# 중복된 수가 여러개 일 수 있고, 임의로 하나를 리턴

# 제약조건: O(n) 이상의 공간 활용불가, 인풋 리스트의 변형불가
def find_same_number(some_list, start=1, end=None):
    if end == None:
        end = len(some_list) - 1
    if start == end:
        return start

    mid = (start + end) // 2  # 중간지점
    left_side = 0

    for num in some_list:
        if start <= num and num <= mid:
            left_side += 1

    if left_side > mid - start + 1:
        return find_same_number(some_list, start, mid)

    return find_same_number(some_list, mid+1, end)         


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
