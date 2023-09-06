import sys
input = sys.stdin.readline

chess = []
for _ in range(8):
    chess.append(list(input().strip()))

dx = [0, 1, -1, 0, 0, 1, 1, -1 ,-1]
dy = [1, 0, 0, -1, 0, -1, 1, 1, -1]

chessPosition = []
emptySpace = [['.'] * 8]

for i in range(8):
    chessPosition.append(emptySpace * i + chess[:8-i])

visited = [[[0] * 8 for _ in range(8)] for _ in range(8)]
ans = 0

def move(count, x, y):
    global ans

    if(count == 8): # 8차례가 지난 후에도 존재하면 도달 가능    
        ans = 1
        return

    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]
        if(0 <= nx < 8 and 0 <= ny < 8 and chessPosition[count][nx][ny] == '.'):
            if(count < 7 and chessPosition[count+1][nx][ny] == '.' and visited[count+1][nx][ny] == 0):
                visited[count+1][nx][ny] = 1
                move(count+1, nx, ny)
            elif(count == 7):
                move(count+1, nx, ny)

move(0, 7, 0)
print(ans)