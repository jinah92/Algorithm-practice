from string import ascii_uppercase

def solution(name):
    answer = 0
    alpa = list(ascii_uppercase)
    cursor = 0

    for i in range(len(name)):
        if name[i] == 'A':
            continue

        input_idx = alpa.index(name[i])
        # 커서 변경
        if cursor != i:
            # 현재 커서 위치가 0이고, 입력 위치가 마지막인 경우
            if cursor == 0 and i == len(name) - 1:
                answer += 1
            else:
                go_left = cursor - i if cursor > i else len(name)-i+cursor
                go_right = i - cursor if i > cursor else len(name)-cursor+i
                answer += min(go_left, go_right)
                cursor = i
        # 알파벳 변경
        answer += min(input_idx, len(alpa) - input_idx)  

    return answer

name = "JAN"
solution(name)