def sum(a, b):
    answer = 0
    tmp = 0

    if a>b:
        tmp = b
        b = a
        a = tmp    

    for i in range(a, b+1):
        answer = answer + i
    return answer

print(sum(3, 5))