import sys
from collections import deque

input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n, k, r = map(int, input().split())

visited = [[0] * (n+1) for _ in range(n+1)]

road = set()
cowPosition = []

cnt = 1

def BFS(x, y):
    global cnt

    q = deque([[x,y]])
    visited[x][y] = cnt

    while(q):
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if(1 <= nx <= n and 1 <= ny <= n and visited[nx][ny] == 0):
                if((cx,cy,nx,ny) in road or (nx,ny,cx,cy) in road):
                    continue
                visited[nx][ny] = cnt
                q.append([nx,ny])
    
    cnt += 1
        
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    road.add((r1,c1,r2,c2))

for _ in range(k):
    r, c = map(int, input().split())
    cowPosition.append([r, c])


for i in range(1, n+1):
    for j in range(1, n+1):
        if(visited[i][j] == 0):
            BFS(i, j)

answer = 0
for i in range(k):
    for j in range(i+1, k):
        cow1_r, cow1_c = cowPosition[i]
        cow2_r, cow2_c = cowPosition[j]
        if(i != j and visited[cow1_r][cow1_c] != visited[cow2_r][cow2_c]):
            answer += 1

print(answer)