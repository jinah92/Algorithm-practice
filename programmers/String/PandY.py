# level 1
# 문자열 내 p와 y의 개수

# URL: https://programmers.co.kr/learn/courses/30/lessons/12916

s = "Pyy"

def solution(s):
    answer = True
    couter = {
        "p": 0,
        "y": 0
    }
    s = s.lower()
    
    for alpa in s:
        if alpa == 'p':
            couter['p'] += 1
        elif alpa == 'y':
            couter['y'] += 1

    if couter['p'] != 0 and couter['y'] != 0:
        if couter['p'] != couter['y']:
            answer = False
        else:
            answer = True
    
    elif couter['p'] == 0 and couter['y'] == 0:
        answer = True
    
    else:
        answer = False

    return answer

print(solution(s))