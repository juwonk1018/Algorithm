# heapq, 그리디 문제

# 가방 당 하나만 가질 수 있으므로 작은 가방부터, 가능한 보석에서 가치가 가장 높은 것만 가져가기.
# 1) 작은 가방에 가치 있는 것을 먼저 선택하게 된다면 이후의 큰 가방에서 선택할 때에도 더 넓은 범위에서 2번째 가치있는 것을 선택가능
# 2) 큰 가방의 범위에서 더 가치 있는 것이 존재한다면, 작은 가방의 범위에서의 보석을 선택하고 이후 큰 가방은 그 보석을 선택 

# heap의 최소값은 맨 앞의 index에 존재한다.

import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewerly = []
bag = []

for _ in range(n):
    weight, value = map(int, input().split())
    jewerly.append([weight, value])

for _ in range(k):
    bag.append(int(input().strip()))

jewerly.sort()
bag.sort()

cur = ans = 0
canSteal = [0] * k

for weight in bag:
    while(cur < len(jewerly) and jewerly[cur][0] <= weight):
        heapq.heappush(canSteal, -jewerly[cur][1])
        cur += 1
    ans -= heapq.heappop(canSteal)

print(ans)