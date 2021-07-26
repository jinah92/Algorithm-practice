# 프린터 큐 : 1966
test_num = int(input())    # 테스트 케이스 수

for _ in range(test_num):
    N, M = list(map(int, input().split(' ')))
    values = list(map(int, input().split(' ')))
    values = [(i, idx) for idx, i in enumerate(values)]
    
    cnt = 0
    while True:
        if values[0][0] == max(values, key=lambda x:x[0])[0]:
            cnt += 1
            if values[0][1] == M:
                print(cnt)
                break
            else:
                values.pop(0)
            
        else:
            values.append(values.pop(0))
