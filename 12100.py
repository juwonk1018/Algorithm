import sys
input = sys.stdin.readline

n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

startPos = [[0, n-2], [n-2, 0], [0, 1], [1, 0]]
dydx = [[0,1],[1,0],[0,-1],[-1,0]] #동, 남, 서, 북
end = [n-1, n-1, 0, 0]

ans = 0

def movePoint(new_board, ny, nx, dir, top):

    dy, dx = dydx[dir]

    if(dir % 2 == 0): #동쪽, 서쪽

        if(new_board[ny][nx] == 0):
            pass
        
        elif(new_board[ny][top] == 0):
            new_board[ny][top] = new_board[ny][nx]
            new_board[ny][nx] = 0

        elif(new_board[ny][top] == new_board[ny][nx]):
            new_board[ny][top] *=2
            new_board[ny][nx] = 0
            top -= dx

        elif(new_board[ny][top] != new_board[ny][nx]):
            top -= dx
            new_board[ny][top] = new_board[ny][nx]
            if(top != nx):
                new_board[ny][nx] = 0
    else:
        if(new_board[ny][nx] == 0):
            pass
        
        elif(new_board[top][nx] == 0):
            new_board[top][nx] = new_board[ny][nx]
            new_board[ny][nx] = 0

        elif(new_board[top][nx] == new_board[ny][nx]):
            new_board[top][nx] *=2
            new_board[ny][nx] = 0
            top -= dy
            
        elif(new_board[top][nx] != new_board[ny][nx]):
            top -= dy
            new_board[top][nx] = new_board[ny][nx]
            if(top != ny):
                new_board[ny][nx] = 0
    return top

def step(new_board, dir, count):
    global ans
    if(count == 5):
        ans = max(ans, max(list(map(max, new_board))))
        return

    ny, nx = startPos[dir]
    dy, dx = dydx[dir]

    if(dir % 2 == 0):
        for _ in range(n):
            top = end[dir]
            nx = startPos[dir][1]
            for _ in range(n-1):
                top = movePoint(new_board, ny, nx, dir, top)
                nx -= dx
            ny += 1

    else:
        for _ in range(n):
            top = end[dir]
            ny = startPos[dir][0]
            for _ in range(n-1):
                top = movePoint(new_board, ny, nx, dir, top)
                ny -= dy
            nx += 1
    

    for i in range(4):
        new_board2 = []
        for j in range(n):
            new_board2.append(new_board[j].copy())
        step(new_board2, i, count+1)

    

for i in range(4):
    new_board = []
    for j in range(n):
        new_board.append(board[j].copy())
    step(new_board, i, 0)


print(ans)

#굳이 4개의 함수를 하나로 묶으려다가 시간 엄청 쓴 느낌..