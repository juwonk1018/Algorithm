from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x, y):
    visited = [[0] * m for _ in range(n)]
    distMap = [[0] * m for _ in range(n)]

    q = deque([[x,y,0]])
    visited[x][y] = 0

    while(q):
        cx, cy, dist = q.popleft()

        distMap[cx][cy] = dist

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if(0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1):
                q.append([nx, ny, dist + 1])
                visited[nx][ny] = 1

    return distMap

n, m = map(int, input().split())

maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))
    
for i in range(n):
    if(2 in maps[i]):
        ans = BFS(i, maps[i].index(2))
        break

for i in range(n):
    for j in range(m):
        if(ans[i][j] == 0 and maps[i][j] == 1):
            ans[i][j] = -1
    print(*ans[i])
