def solution(left, right):
    total_sum = 0 # 리턴 값
    for num in range(left, right+1):
        div_num = 0  # 약수의 개수
        for i in range(1, num+1):
            if num % i == 0:
                div_num += 1
        total_sum += num * ( -1 if div_num % 2 else 1)
    return total_sum