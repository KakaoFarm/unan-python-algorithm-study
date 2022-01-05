# 숫자 카드 게임
import random
N, M = list(map(int, input().split()))

def game(N,M):
    matrix = []
    for i in range(N):
        x = []
        for j in range(M):
            x.append(random.randint(1,10))
        matrix.append(x)

    cards = []
    n = 1
    for k in matrix:
        cards.append(min(k))
        print('player{0}가 뽑은 카드는 {1}입니다.'.format(n,min(k)))
        n += 1

    win_card = max(cards)
    if cards.count(max(cards)) != 1:
        return '무승부가 발생했습니다.'
        
    else:
        return '승리 : player{0}, 뽑은 카드 : {1}'.format((cards.index(win_card) + 1), win_card)

print(game(N,M))