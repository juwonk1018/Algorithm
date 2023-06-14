import sys
input = sys.stdin.readline

n, m = map(int, input().split())

switch = [[[] for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    x, y, a, b = map(int, input().split())
    switch[x][y].append([a,b])



roomStatus = [[[0,0] for _ in range(n+1)] for _ in range(n+1)] # [visited, lightOnOff]
roomStatus[1][1] = [1, 1]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = [[1, 1]]

while(q):
    cx, cy = q.pop()

    for nx, ny in switch[cx][cy]:
        if(roomStatus[nx][ny][1] == 0): # 스위치를 누른 방에 불이 켜지지 않았다면
            roomStatus[nx][ny][1] = 1
            for i in range(4):
                nnx, nny = nx + dx[i], ny + dy[i]
                if(1 <= nnx <= n and 1 <= nny <= n and roomStatus[nnx][nny][0]):
                    roomStatus[nx][ny][0] = 1
                    q.append([nx,ny])
                    break
    
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if(1 <= nx <= n and 1 <= ny <= n and roomStatus[nx][ny][0] == 0 and roomStatus[nx][ny][1] == 1):
            q.append([nx, ny])
            roomStatus[nx][ny][0] = 1

answer = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        answer += roomStatus[i][j][1]

print(answer)