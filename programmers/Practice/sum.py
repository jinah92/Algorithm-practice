def sum(a, b):
    answer = 0

    for i in range(a, b+1):
        answer = answer + i
    return answer

print(sum(3, 5))