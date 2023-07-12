from collections import deque
import sys

input = sys.stdin.readline

def isDroppable(x, y):
    droppable = True
    visited = set()
    visited.add((x,y))
    q = deque([[x,y]])
    
    while(q):
        cx, cy = q.popleft()
        if(cx == r-1):
            droppable = False

        for nx, ny in [[cx+1, cy], [cx, cy+1], [cx-1, cy], [cx, cy-1]]:
            if(0 <= nx < r and 0 <= ny < c and cave[nx][ny] == 'x' and (nx, ny) not in visited):
                visited.add((nx,ny))
                q.append([nx,ny])

    return [droppable, visited]

def calculateHeight(visitedList):

    ans = float("INF")
    for x, y in visitedList:
        for j in range(x+1, r):
            if(0<= j < r):
                if(cave[j][y] == 'x' and (j,y) not in visitedList):
                    ans = min(ans, j - x - 1)
                    break
                elif(j == r-1 and cave[j][i] == '.'):
                    ans = min(ans, j - x)
                    break
    
    return ans 

def removeMineral(x, y):
    cave[x][y] = '.'
    for nx, ny in [[x-1,y], [x, y+1], [x, y-1], [x+1,y]]:
        if(0 <= nx < r and 0 <= ny < c):
            if(cave[nx][ny] == 'x'):
                booleanDrop, visitedList = isDroppable(nx,ny)
                if(booleanDrop):
                    h = calculateHeight(visitedList)
                    for cx, cy in visitedList:    
                        cave[cx][cy] = '.'

                    for cx, cy in visitedList:    
                        cave[cx+h][cy] = 'x'
                    
r, c = map(int, input().split())

cave = [[''] * c for i in range(r)]
                
for i in range(r):
    row = input().strip()
    for j in range(c):
        cave[i][j] = row[j]

n = int(input())
throwList = list(map(int, input().split()))

for i in range(n):
    if(i%2 == 0): #Left
        for j in range(c):
            if(cave[r-throwList[i]][j] == 'x'):
                removeMineral(r-throwList[i], j)
                break

    else: #Right
        for j in range(c-1,-1,-1):
            if(cave[r-throwList[i]][j] == 'x'):
                removeMineral(r-throwList[i], j)
                break

for i in range(r):
    print(''.join(cave[i]))