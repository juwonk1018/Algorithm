import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
redPos = bluePos = [0,0]

for i in range(n):
    board.append(input().strip())
    if('R' in board[i]):
        redPos = [i, board[i].index('R')]
    if('B' in board[i]):
        bluePos = [i, board[i].index('B')]

def strReplace(board, y, x, chr):
    board[y] = board[y][:x] + chr + board[y][x+1:]

pos = [[-1, 0], [0, 1], [1, 0], [0, -1]]

ans = float("inf")
def gravity(dir, num, board, red, blue):
    global ans
    if(ans < num or num > 10):
        return

    new_board = []
    for i in range(0,n):
        new_board.append(board[i])

    change = False
    result = False
    dy, dx = pos[dir]

    nextRed = [red[0], red[1]]
    nextBlue = [blue[0], blue[1]]
    for _ in range(max(n-2, m-2)):
        oy, ox = nextRed[0], nextRed[1]
        ny, nx = nextRed[0] + dy, nextRed[1] + dx
        
        if(new_board[ny][nx] == "."):
            strReplace(new_board, ny,nx,"R")
            strReplace(new_board, oy,ox,".")
            nextRed = [ny, nx]
            change = True
        elif(new_board[ny][nx] == "O"):
            strReplace(new_board, oy,ox,".")
            result = True

        oy, ox = nextBlue[0], nextBlue[1]
        ny, nx = nextBlue[0] + dy, nextBlue[1] + dx
        if(new_board[ny][nx] == "."):
            strReplace(new_board, ny,nx,"B")
            strReplace(new_board, oy,ox,".")
            nextBlue = [ny, nx]
            change = True
        elif(new_board[ny][nx] == "O"):
            strReplace(new_board, oy,ox,".")
            return
    
    if(result == True):
        ans = min(ans, num)

    if(change == True):
        for i in range(4):
              if(i != dir):
                  gravity(i, num+1, new_board, nextRed, nextBlue)
    
for i in range(4):
    gravity(i, 1, board, redPos, bluePos)

if(ans == float("INF")):
    print(-1)
else:
    print(ans)