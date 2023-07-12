import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)
n, m = map(int, input().split())

def checkOffice(idx, cnt):
    global answer

    if(idx == num):
        answer = min(answer, cnt)
        return
        
    cx, cy = cctvPosition[idx]

    officeCopy = [office[i] for i in range(n)]

    for i in range(4):
        changeList = []
        for d in cctvDirection[idx]:
            dx, dy = direction[(d+i)%4]
            for j in range(max(n,m)):
                nx, ny = cx + dx * j, cy + dy * j
                if(0 <= nx < n and 0 <= ny < m and office[nx][ny] == 0):
                    office[nx][ny] = -1
                    changeList.append([nx,ny])
                elif(0 <= nx < n and 0 <= ny < m and office[nx][ny] == 6):
                    break

        checkOffice(idx+1, cnt - len(changeList))

        for x, y in changeList:
            office[x][y] = 0

office = []
direction = [[-1,0],[0,1],[1,0],[0,-1]]
cctvPosition = []
cctvDirection = []

entireSpace = 0

for _ in range(n):
    office.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if(1 <= office[i][j] <= 5):
            cctvPosition.append([i,j])
            if(office[i][j] == 1):
                cctvDirection.append([1])
            elif(office[i][j] == 2):
                cctvDirection.append([1,3])
            elif(office[i][j] == 3):
                cctvDirection.append([0,1])
            elif(office[i][j] == 4):
                cctvDirection.append([0,1,3])
            elif(office[i][j] == 5):
                cctvDirection.append([0,1,2,3])

        elif(office[i][j] == 0):
            entireSpace += 1

answer = entireSpace
num = len(cctvPosition)
checkOffice(0, entireSpace)
    
print(answer)