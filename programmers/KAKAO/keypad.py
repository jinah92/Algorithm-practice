# 키패드 누르기 (레벨 1)
# https://programmers.co.kr/learn/courses/30/lessons/67256

dict_num = {
    1 : (0, 0),
    2 : (0, 1),
    3 : (0, 2),
    4 : (1, 0),
    5 : (1, 1),
    6 : (1, 2),
    7 : (2, 0),
    8 : (2, 1),
    9 : (2, 2),
    '*' : (3, 0),
    0 : (3, 1),
    '#' : (3, 2)
}

def center_diff(number, key_loc):

    num1 = dict_num[number]
    num2 = dict_num[key_loc]
    return abs(num1[0]-num2[0]) + abs(num1[1]-num2[1])
         
    

def solution(numbers, hand):
    answer = ''
    r, l = '#', '*'
    r_diff, l_diff = 0, 0

    for number in numbers:
        data = ''
        if number in (1, 4, 7):
            data = 'L'
        elif number in (3, 6, 9):
            data = 'R'
        else:
           r_diff = center_diff(number, r)
           l_diff = center_diff(number, l)
           if r_diff > l_diff:
               data = 'L'
           elif r_diff < l_diff:
               data = 'R'
           else:
               if hand == 'right':
                   data = 'R'
               else:
                   data = 'L'
        
        if data == 'R':
            r = number
        else:
            l = number
        
        answer += data
    return answer