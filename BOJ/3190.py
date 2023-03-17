from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())



board = [[0] * (n+1) for _ in range(n+1)] # 0은 빈 공간, 1은 snake, 2는 apple
board[1][1] = 1
for _ in range(k):
    y, x = map(int, input().split())
    board[y][x] = 2

l = int(input())

command = deque()
for _ in range(l):
    time, d = input().strip().split()
    command.append([time, d])

snakePos = deque([[1,1]]) #현재 뱀의 위치
curDir = 1

dir = [[-1,0],[0,1],[1,0],[0,-1]]

time = 0
while(True):
    time += 1
    # 머리를 다음칸에 옮길 수 있는 지(몸을 만나거나 벽을 만남) 확인 후 사과의 여부에 따라 행동
    hy, hx = snakePos[0]
    ny, nx = hy + dir[curDir][0], hx + dir[curDir][1]
    if(not(0 < ny <= n) or not(0 < nx <= n) or board[ny][nx] == 1):
        print(time)
        break
        
    snakePos.appendleft([ny, nx]) #머리를 다음칸에 위치
    
    if(board[ny][nx] == 2): # 사과를 먹었다면
        board[ny][nx] = 1 # 사과를 없애고 해당 자리를 snake의 자리로 표기
    
    else:
        board[ny][nx] = 1
        ty, tx = snakePos.pop() # 꼬리의 위치를 보드와 현재 뱀의 위치에서 제거
        board[ty][tx] = 0
        

    # 시간 종료 후 명령확인
    if(command and time == int(command[0][0])): #가장 앞선 명령의 시간이 이 시점이라면
        t, nd = command.popleft()
        
        if(nd == 'L'): #왼쪽으로 방향 전환
            curDir = (curDir - 1) % 4
        elif(nd == 'D'): #오른쪽으로 방향 전환
            curDir = (curDir + 1) % 4

    