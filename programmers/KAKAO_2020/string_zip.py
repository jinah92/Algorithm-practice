def solution(s):
    answer = s
    current_char = ""

    for i in range(1, int(len(s)-1/2)):
        current_char = s[:i]  # s[0]   s[0:1]
        count = 0
        current_answer = ''
        for j in range(0, len(s), i):
            if current_char == s[j:j+i]:      # 연속된 두 문자가 동일할 경우
                count = count+1            # 문자 반복 수를 1 증가
            else:
                if count != 1:
                    current_answer = f'{current_answer}{count}{current_char}'
                else:
                    current_answer = f'{current_answer}{current_char}'

                current_char = s[j:j+i]
                count = 1
        if count != 1:
            current_answer = f'{current_answer}{count}{current_char}'
        else:
            current_answer = f'{current_answer}{current_char}'
        if len(answer) > len(current_answer):
            answer = current_answer

    return len(answer)


if __name__ == "__main__":
    test = solution("aabbcc")
    print(test)
