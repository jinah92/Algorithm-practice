# n : 전체 학생 수, lost : 체육복을 도난 당한 학생들의 번호, reverse : 여벌의 체육복을 가져온 학생 번호
def solution(n, lost, reserve):
    answer = 0
    uniform_list = list([i for i in range(1,n+1)])

    for j in range(n):
        for t in range(n):
            if n == lost[j]:
                break
            else:
                uniform_list.append(t)
                break
        
        for j in len(reserve):
            if t == reserve[j]:
                break
            else:
                pass

    print(uniform_list)

    for i in len(reserve):
        for j in len(lost):
            if (reserve[len(reserve)-i-1] - lost[j] == 1):
                uniform_list.append(lost[j])

            elif reserve[i] - lost[j] == -1:
                pass
            else:
                break
                
                

        
    return answer


solution(5, [2, 4], [1, 3, 5])   # return = 5