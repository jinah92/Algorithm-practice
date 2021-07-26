N, M = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))

max_val = 0
cards.sort(reverse=True)

for i in range(0, len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if cards[i] + cards[j] + cards[k] <= M:
                max_val = max(max_val, cards[i] + cards[j] + cards[k])

print(max_val)
    