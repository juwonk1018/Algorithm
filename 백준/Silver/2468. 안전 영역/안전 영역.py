import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

m = max(map(max, arr))

dx = [0,1,-1,0]
dy = [1,0,0,-1]

ans = 0
for k in range(m+1):
    for i in range(n):
        for j in range(n):
            if(arr[i][j] <= k):
                arr[i][j] = 0

    visited = [[False] * n for _ in range(n)]
    
    count = 0
    for i in range(n):
        for j in range(n):
            if(visited[i][j] == False and arr[i][j] > 0):
                
                q = deque([[i,j]])
                while(q):
                    cx, cy = q.popleft()
                    for l in range(4):
                        nx, ny = cx + dx[l], cy + dy[l]
                        if(0<=nx<n and 0<=ny<n and visited[nx][ny] == False and arr[nx][ny]):
                            q.append([nx,ny])
                            visited[nx][ny] = True

                count += 1
    ans = max(count, ans)

print(ans)