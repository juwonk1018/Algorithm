import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,1,-1,0,1,-1]


s = set()

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if(arr[i][j] == 1):
            s.add((i,j))

count = 0

while(s):
    ns = set()
    for cx, cy in s:
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if(0<=nx<n and 0<=ny<m and visited[nx][ny] == False and arr[nx][ny] == 0):
                ns.add((nx,ny))
                visited[nx][ny] = True
    s = ns
    count += 1

print(count-1)