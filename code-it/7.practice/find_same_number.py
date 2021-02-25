# 중복된 수를 리턴하는 함수  (non-brute force)
# 중복된 수가 여러개 일 수 있고, 임의로 하나를 리턴
def find_same_number(some_list):
    obj = {}
    for num in some_list:
        if num in obj:
            return num
        obj[num] = 1

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
