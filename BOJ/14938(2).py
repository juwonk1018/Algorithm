#워셜-플로이드 알고리즘을 이용한 풀이

import sys
import heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
cost = [[float("INF")] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    cost[a][b] = min(cost[a][b], l)
    cost[b][a] = min(cost[b][a], l)
    
for i in range(1, n+1):
    cost[i][i] = 0

for c in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost[a][b] = min(cost[a][b], cost[a][c] + cost[c][b])

ans = 0
for i in range(1, n+1):
    s = 0
    for j in range(1, n+1):
        if(cost[i][j] <= m):
            s += item[j-1]
    ans = max(s, ans)
print(ans)