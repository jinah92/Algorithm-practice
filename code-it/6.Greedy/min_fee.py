# 최소 벌금을 리턴 (페이지 1장당 1분씩 지각)
# pages_to_print : 출력할 페이지 수를 담은 리스트

def min_fee(pages_to_print):
    min_fee = []
    previous_time = 0
    for page in sorted(pages_to_print):
        min_fee.append(previous_time+page)
        previous_time += page
    
    return sum(min_fee)


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))

