def solution(s) :
    answer = []
    if(len(s)%2 == 0):   # 단어길이가 짝수
        answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
        print(answer)
    
    else:
        answer.append(s[int(len(s)/2)])
    return answer
