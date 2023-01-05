from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    bus[s].append([e,c])

start, end = map(int, input().split())

dijkstra = [float("INF")] * (n+1)
dijkstraRoute = [[] for _ in range(n+1)]
dijkstra[start] = 0
dijkstraRoute[start] = [start]

q = deque()
q.append(start)
visited = [0] * (n+1)


while(q):
    cur = q.popleft()
    visited[cur] = 1
    print(cur)
    for e, c in bus[cur]:
        if(dijkstra[e] > dijkstra[cur] + c):
            dijkstra[e] = dijkstra[cur] + c
            dijkstraRoute[e] = dijkstraRoute[cur] + [e]
    
    minCost = float("INF")
    nextVertex = 0
    for i in range(n+1):
        if(visited[i] == 0 and dijkstra[i] < minCost):
            minCost = dijkstra[i]
            nextVertex = i
    if(nextVertex):
        q.appendleft(nextVertex)

print(dijkstra)
ans = dijkstra[end]
ans_route = dijkstraRoute[end]

print(ans, len(ans_route), sep = "\n")
print(*ans_route, sep = " ")