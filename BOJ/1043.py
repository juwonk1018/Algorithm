# set을 활용하면 깔끔하게 표기가 가능함

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
party = []

who = set(list(map(int, input().split()))[1:])

for _ in range(m):
    cur = list(map(int, input().split()))
    party.append(set(cur[1:]))

lie = [1] * (m)

for _ in range(m): #파도타기를 할 경우에 최악의 경우 m번을 해야됨
    for i in range(m):
        if(lie[i] and who & party[i]): #아는 사람이 존재한다면
            lie[i] = 0
            who = who.union(party[i])
            break

print(sum(lie))