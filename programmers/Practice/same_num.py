def Samenumber(arr):
    answer = []
    
    answer.append(arr[0])

    for i in range(0, len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])

    return answer