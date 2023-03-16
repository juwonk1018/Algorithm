# 구현 - 시간이 많이 걸린 문제
# 왼쪽, 오른쪽으로 이동하든 0, c-1에서 턴하는 것은 똑같으므로 [-c, c-1]의 범위에서 이동 형태가 반복된다. 
# 신경쓸 부분은 이동 위치에 따라 c-1인 경우에 방향은 속도가 0이지 않은 이상 오른쪽으로 고정이므로 등호를 왼쪽, 오른쪽 다르게 설정해야 된다.

import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())

grid = [[0] * (c) for _ in range(r)]
pos = -1; score = 0

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    grid[x-1][y-1] = [s,d,z] #속도, 방향, 크기


def catchShark(): #return 사용 시 break를 쓰지 않아도 됨
    global pos, score
    pos += 1
    for i in range(r):
        if(grid[i][pos] != 0):
            score += grid[i][pos][2]
            grid[i][pos] = 0
            break


def moveShark():
    global grid
    newGrid = [[0] * (c) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            
            if(grid[i][j] != 0): #속도가 0이면, 상어가 이동해서는 나올 수 없는 방향이 나올 수도 있어서 그대로 유지 
                nR = i; nC = j; nD = grid[i][j][1]
                # 2 * r - 2 - nR + grid[i][j][0]을 nextPos로 하면 2*r -2의 나머지를 구해 아래로 이동하는 경우와 동일하게 [0,r-1]으로 통합시킬 수 잇음
                if(grid[i][j][1] == 1): #위로 이동       
                    nextPos = (nR - grid[i][j][0]) % (2*r - 2)
                    if(nextPos >= r - 1): # 아래로 이동하는 경우
                        nR = 2 * r - 2 - nextPos; nD = 2
                    elif(nextPos < r - 1): # 위로 이동하는 경우
                        nR = nextPos; nD = 1
                        
                elif(grid[i][j][1] == 2): #아래로 이동                    
                    nextPos = (nR + grid[i][j][0]) % (2*r - 2)
                    if(nextPos > r - 1): #위로 이동하는 경우
                        nR = 2 * r - 2 - nextPos; nD = 1
                    elif(nextPos <= r - 1): #아래로 이동하는 경우[0, r-1]
                        nR = nextPos; nD = 2
                
                #오른쪽으로 이동 시, c-1의 지점에서 오른쪽으로 설정해야 돼서 밑에 <=
                #왼쪽 이동 시, c-1의 지점에서 오른쪽 설정 때문에 위에서 >=
                elif(grid[i][j][1] == 3): #오른쪽으로 이동                    
                    nextPos = (nC + grid[i][j][0]) % (2*c - 2)
                    if(nextPos > c - 1): #왼쪽으로 이동하는 경우
                        nC = 2 * c - 2 - nextPos; nD = 4
                    elif(nextPos <= c - 1): #오른쪽으로 이동하는 경우
                        nC = nextPos; nD = 3


                elif(grid[i][j][1] == 4): #왼쪽으로 이동
                    nextPos = (nC - grid[i][j][0]) % (2*c - 2)
                    if(nextPos >= c - 1): #오른쪽으로 이동하는 경우
                        nC = 2 * c - 2 - nextPos; nD = 3
                    elif(nextPos < c - 1): #왼쪽으로 이동하는 경우
                        nC = nextPos; nD = 4 
                    
                if(grid[i][j][0] == 0): #속도가 0이라면, 방향은 그대로
                    nD = grid[i][j][1]

                if(newGrid[nR][nC] != 0):
                    if(newGrid[nR][nC][2] < grid[i][j][2]): #기존보다 크기가 크다면 잡아먹음
                        newGrid[nR][nC] = [grid[i][j][0], nD, grid[i][j][2]]
                else:
                    newGrid[nR][nC] = [grid[i][j][0], nD, grid[i][j][2]]
                
                
    for i in range(len(newGrid)): #기존 격자판에 copy
        grid[i] = newGrid[i].copy()
        

for _ in range(c):
    catchShark()
    moveShark()

print(score)