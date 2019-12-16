import operator

answer_1 = [1, 2, 3, 4, 5]
answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    students = {
        '1' : 0,
        '2' : 0,
        '3' : 0
    }

    result = []

    for i in range(len(answers)):
        if answer_1[i%len(answer_1)] == answers[i]:
            # correct_answers[0] = correct_answers[0] + 1
            students['1'] = students['1'] + 1
                
        if answer_2[i%len(answer_2)] == answers[i]:
            # correct_answers[1] = correct_answers[1] + 1
            students['2'] = students['2'] + 1
                
        if answer_3[i%len(answer_3)] == answers[i]:
            # correct_answers[2] = correct_answers[2] + 1
            students['3'] = students['3'] + 1

    # students.values().sort()
    # students_test = students.items()
    students_test = sorted(students.items(), key=lambda x: x[1], reverse=True)
                
    for key, value in students_test.items():
        if value !=0:
            result.append(students_test[key])
    return result

answers = [1, 2, 3, 4, 5, 1, 2]

test = solution(answers)
print(test)