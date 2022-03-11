from itertools import permutations
import sys

def solution():
    sys.stdin = open('input.txt', 'r')

    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    
    cards = []

    for _ in range(n):
        cards.append(int(sys.stdin.readline()))

    hubo_cards = []
    picked_cards = list(permutations(cards, k))
    for tuple in picked_cards:
        number = ''
        for card in tuple:
            number += str(card)
        
        if number not in hubo_cards:
            hubo_cards.append(number)
        
    print(len(hubo_cards))


if __name__ == "__main__":
    solution()