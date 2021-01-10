# level 1
# 최대공약수와 최소공배수
# url : https://programmers.co.kr/learn/courses/30/lessons/12940

def UC(X, Y):
    while(Y):
        X, Y = Y, X%Y

    return X

def LCM(X, Y, UC):
    return (X*Y) // UC

def solution(n, m):    
    answer = [UC(n, m), LCM(n, m, UC(n, m))]

    return answer