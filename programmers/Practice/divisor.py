def divisor(arr, divisor):
    answer = []

    for i in range(0, len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])

    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    
    return answer

print(divisor([5, 9, 7, 10],5))