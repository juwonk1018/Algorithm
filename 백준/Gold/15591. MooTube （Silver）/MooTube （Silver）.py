# 플로이드-워셜 = 시간초과
# 미리 정점간의 거리를 계산하는 것은 O(n * (V + E))로 시간 초과가 발생.
# O(V + E)는 모든 edges를 탐색하면서 모든 vertexs가 queue에 들어가기 때문에 O(V+E) 
# 하지만, 각 질문마다 k를 넘는지 확인하는 작업은 모든 edge를 

import sys
from collections import deque

input = sys.stdin.readline

n, Q = map(int, input().split())

edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, q, r = map(int, input().split())

    edges[p].append((q,r))
    edges[q].append((p,r))

        
def bfs(k,v):
    q = deque([v])
    visited = [0] * (n+1)
    visited[v] = 1

    num = 0

    while(q):
        cur = q.popleft()
        for dest, nextUsado in edges[cur]:
            if(visited[dest] == 0 and nextUsado >= k):
                visited[dest] = 1
                q.append(dest)
                num += 1

    return num

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k,v))