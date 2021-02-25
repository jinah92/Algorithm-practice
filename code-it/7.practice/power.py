# 거듭제곱을 계산하는 함수 
def power(x, y):
    # Base Case
    if y == 0:
        return 1

    # 동일한 값을 한번만 계산
    sub_power = power(x, y // 2)

    if y % 2 == 0:
        # Recursive Case
        return sub_power * sub_power
    else:
        return x * sub_power * sub_power


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
