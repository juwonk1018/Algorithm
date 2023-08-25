# 플로이드-워셜 = 시간초과

import sys
from collections import deque

input = sys.stdin.readline

n, Q = map(int, input().split())

edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, q, r = map(int, input().split())

    edges[p].append([q,r])
    edges[q].append([p,r])

        
for _ in range(Q):
    k, v = map(int, input().split())

    q = deque([[v, float("INF")]])
    visited = [0] * (n+1)
    visited[v] = 1

    num = 0
    while(q):
        cur, usado = q.popleft()
        for dest, nextUsado in edges[cur]:
            nextUsado = min(usado, nextUsado)
            if(visited[dest] == 0 and nextUsado >= k):
                visited[dest] = 1
                q.append([dest, nextUsado])
                num += 1

    print(num)