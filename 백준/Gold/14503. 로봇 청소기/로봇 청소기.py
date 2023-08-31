import sys
input = sys.stdin.readline

n, m = map(int, input().split())

r, c, d = map(int, input().split())

dr = [-1,0,1,0]
dc = [0,1,0,-1]
robotPosition = [r,c]
robotDirection = d

roomStatus = []

for _ in range(n):
    roomStatus.append(list(map(int, input().split())))

ans = 0

while(True):
    r, c= robotPosition
    if(roomStatus[r][c] == 0): # STEP 1
        roomStatus[r][c] = 2
        ans += 1

    hasDirtySpace = False
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if(roomStatus[nr][nc] == 0):
            hasDirtySpace = True

    if(hasDirtySpace == False): # STEP 2
        rr, rc = dr[robotDirection] * -1, dc[robotDirection] * -1 # 후진 방향
        
        if(roomStatus[r+rr][c+rc] != 1):
            robotPosition = [r+rr, c+rc]
        else:
            break

    elif(hasDirtySpace == True): # STEP 3
        robotDirection = (robotDirection - 1) % 4
        nr, nc = robotPosition[0] + dr[robotDirection], robotPosition[1] + dc[robotDirection]
        if(roomStatus[nr][nc] == 0):
            robotPosition = [nr, nc]


print(ans)