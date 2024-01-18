from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

n1, n2 = map(int, input().split())

m = int(input())

edge = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)

q = deque([n1])

visited = [-1] * (n+1)
visited[n1] = 0

while(q):
    cx = q.popleft()
    for nx in edge[cx]:
        if(visited[nx] == -1): # 방문한 적이 없으면
            visited[nx] = visited[cx] + 1
            q.append(nx)

    if(visited[n2] != -1):
        break

print(visited[n2])