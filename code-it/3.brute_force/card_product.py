def max_product(left_cards, right_cards):
    max_val = 0
    for num_1 in left_cards:
        for num_2 in right_cards:
            if (num_1 * num_2) > max_val:
                max_val = num_1*num_2

    return max_val


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))