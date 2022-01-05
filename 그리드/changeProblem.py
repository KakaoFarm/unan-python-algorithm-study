'''
당신은 음식점의 계산을 도와주는 점원이다.
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리
동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야할 돈이
N원일 때 거슬러줘야할 동전의 최소 개수를 구하라. 거슬러 줘야할 돈 N은 항상 10의 배수이다.

'''


import sys
N = int(sys.stdin.readline().rstrip())

def change2(money):
    n = [500,100,50,10]
    number = 0
    for i in n:
        number += money // i
        money %=  i
        if money == 0:
            break

    return number

print(change2(N))