# 정렬된 리스트를 받아서, 임의의 두 수의 합이 search_sum이 되는지를 판단하는 함수

def sum_in_list(search_sum, sorted_list):
    idx_1, idx_2 = 0, len(sorted_list)-1
    
    while(idx_1 != idx_2):
        tmp_sum = sorted_list[idx_1] + sorted_list[idx_2]
        if tmp_sum == search_sum:
            return True
        else:
            if tmp_sum > search_sum:
                idx_2 -= 1
            else:
                idx_1 += 1

    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
