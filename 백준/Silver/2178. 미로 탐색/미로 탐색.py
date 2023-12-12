import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

arr = []

for _ in range(n):
    arr.append(list(map(int, input().strip())))

visited = [[float("INF")] * m for _ in range(n)]

q = deque([[0,0]])
visited[0][0] = 1

while(q):
    cx, cy = q.popleft()

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if(0 <= nx < n and 0 <= ny < m):
            if(arr[nx][ny] == 1 and visited[cx][cy] + 1 < visited[nx][ny]):
                visited[nx][ny] = visited[cx][cy] + 1
                q.append([nx,ny])

print(visited[n-1][m-1])