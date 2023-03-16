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

cur = [[0,0]]

cnt = 0
while(cur):
    x, y = cur.pop()
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if(0 <= nx < n and 0 <= ny < m):
            
            if(visited[nx][ny] == -1 and maze[nx][ny] == 0):
                visited[nx][ny] = visited[x][y]
                cur.append([nx,ny])
                
            if(maze[x][y] == 0):
                if(visited[nx][ny] == -1 and maze[nx][ny] == 1):
                    visited[nx][ny] = visited[x][y] + 1
                    cur.append([nx,ny])
    
print(visited)