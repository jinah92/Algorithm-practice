answer_1 = [1, 2, 3, 4, 5]
answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    students = {1 : 0, 2 : 0, 3 : 0}
    result = []
    highscore = 0

    for i in range(len(answers)):
        if answer_1[i%len(answer_1)] == answers[i]:
            students[1] = students[1] + 1
                
        if answer_2[i%len(answer_2)] == answers[i]:
            students[2] = students[2] + 1
                
        if answer_3[i%len(answer_3)] == answers[i]:
            students[3] = students[3] + 1

    students_test = sorted(students.items(), key=lambda x: x[1], reverse=True)
    
    highscore = students_test[0]
    same = []

    for value in students_test:
        if value[1] != 0:
            if (value[1] == highscore[1]):
                same.append(value[0])
            else:
                result.append(value[0])



    return same