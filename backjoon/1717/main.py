import sys

parents = {}
inputs = []

def find_parent(p):
    if p == parents[p]:
        return p
    else:
        _p = find_parent(parents[p])
        parents[p] = _p
        return _p

def solution():
    sys.stdin = open('input.txt', 'r')
    n,m = map(int, sys.stdin.readline().split())

    # n, m = list(map(int, input().split()))
    # inputs = []

    for j in range(m):
        check, item_1, item_2 = list(map(int, input().split()))
        inputs.append([check, item_1, item_2])

    for i in range(n+1):
        parents[i] = i

    for j in range(m):
        check, item_1, item_2 = inputs[j]
        
        if check == 1:
            if find_parent(item_1) == find_parent(item_2):
                print('YES')
            else: print('NO')
        else:
            p1 = find_parent(item_1)
            p2 = find_parent(item_2)
            parents[p2] = p1


if __name__ == "__main__":
    solution()

