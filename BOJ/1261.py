# 첫 방법을 0일때는 visited[x][y], 1일때 visited[x][y] + 1이었는데,
# 여기서 0일 경에는 좌표를 appendleft([nx,ny])로 하면 풀린 문제
# 가까운 것을 먼저 appendleft로 처리하는 것이 [다익스트라 알고리즘] 의 개념이어서 태그인듯.

from collections import deque

import sys
input = sys.stdin.readline

dxdy = [[-1,0], [0,1], [1,0], [0,-1]]

m, n = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))
    
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0

cur = [[0,0]]; nextList = []


# cycle을 돌면서 count를 올리는데, 0인 위치는 count와 같이, 1인 위치는 cnt+1로 기록

cnt = 0
while(visited[n-1][m-1] == -1):
    while(cur):
        x, y = cur.pop()
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if(0 <= nx < n and 0 <= ny < m):
                if(visited[nx][ny] == -1 and maze[nx][ny] == 0):
                    visited[nx][ny] = cnt
                    cur.append([nx,ny])
                elif(visited[nx][ny] == -1 and maze[nx][ny] == 1):
                    visited[nx][ny] = cnt + 1
                    nextList.append([nx,ny])

    cur = nextList.copy()
    nextList = []
    cnt += 1

print(visited[n-1][m-1])
