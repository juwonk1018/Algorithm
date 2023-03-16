# 하나의 배열에 물, 고슴도치의 위치를 넣어도 무관

import sys
input = sys.stdin.readline

r,c = map(int, input().split())

m = []
dest = []
hedgePos = set() # [y, x, cnt]
waterPos = set()

for i in range(r):
    line = input().split()[0]
    for j in range(len(line)):
        if(line[j] == 'S'):
            hedgePos.add((i,j))
        if(line[j] == '*'):
            waterPos.add((i,j))
        if(line[j] == 'D'):
            dest = [i,j]
    m.append(line)

dydx = [[1,0], [-1,0], [0,1], [0,-1]]


visited = [[False] * c for _ in range(r)]



def findCave():
    global hedgePos, waterPos, dest

    cnt = 0
    while(hedgePos):
        # 고슴도치가 이동할 수 있는 곳을 탐색
        nextHedgePos = set()
        for y, x in hedgePos: 
            visited[y][x] = True # 방문 처리
            for dy, dx in dydx:
                ny = y + dy; nx = x + dx
                if(0 <= ny < r and 0 <= nx < c and visited[ny][nx] == False):                
                    if(m[ny][nx] == '.'):
                        nextHedgePos.add((ny, nx))
                    elif([ny, nx] == dest):
                        return cnt + 1
        
        # 물의 이동
        nextWaterPos = set()
        for y, x in waterPos:
            for dy, dx in dydx:
                ny = y + dy; nx = x + dx
                if(0 <= ny < r and 0 <= nx < c):
                    if(m[ny][nx] == '.'):
                        m[ny] = m[ny][:nx] + '*' + m[ny][nx+1:]
                        nextWaterPos.add((ny,nx))
                    if((ny, nx) in nextHedgePos):
                        nextHedgePos.remove((ny,nx))

                    
        hedgePos = nextHedgePos
        waterPos = nextWaterPos
        cnt += 1
        
    return 0

ans = findCave()
print(ans if ans else "KAKTUS")