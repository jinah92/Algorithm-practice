
#데이터 입력
q_num = 4

# 함수 형태
def n_qeen(num) :

    matrix = [[0]*num for i in range(num)]

    # 스택
    stack = []
    # Queen의 위치
    count = 0

    # 체스판 가로
    for i in num-1:
        # 체스판 세로
        for j in num:
            stack.append(matrix[i][j])



    return count