# 0,1 번 행에 블록이 존재하는지 체크하고, board에 [[0,0,0,0]] * cnt로 추가를 하니
# shallow copy가 되어 둘 중 값을 하나만 수정해도 모두 수정되는 현상. => 유의

import sys
input = sys.stdin.readline

n = int(input())

def dropBlock(t, x, y, targetBoard):
    if(t == 1):
        pos = 5
        for i in range(5, -1, -1):
            if(targetBoard[i][y] == 0):
                pos = i
            else:
                break
        targetBoard[pos][y] = 1
        return

    elif(t == 2):
        pos = 5
        
        for i in range(5, -1, -1):
            if(targetBoard[i][y] == 0 and targetBoard[i][y+1] == 0):
                pos = i
            else:
                break
                
        targetBoard[pos][y] = 1
        targetBoard[pos][y+1] = 1
        
        return

    elif(t == 3):
        pos = 4
        for i in range(4, -1, -1):
            if(targetBoard[i][y] == 0 and targetBoard[i+1][y] == 0):
                pos = i
            else:
                break
        targetBoard[pos][y] = 1
        targetBoard[pos+1][y] = 1
        return

def checkBoard(targetBoard):
    global score
    for i in range(3, -1, -1):
        if(sum(targetBoard[i]) == 4): # 완성되는지 체크
            targetBoard = targetBoard[:i] + targetBoard[i+1:] + [[0,0,0,0]]
            score += 1

    cnt = 0
    for i in range(4,6):
        if(sum(targetBoard[i]) != 0): # 0,1번 행과 열에 존재하는지 체크
            cnt += 1

    targetBoard = targetBoard[cnt:]
    for i in range(cnt):
        targetBoard += [[0,0,0,0]]
        
    return targetBoard


greenBoard = [[0] * 4 for _ in range(6)]
blueBoard = [[0] * 4 for _ in range(6)]

score = 0

for i in range(n):
    t, x, y = map(int, input().split())
    dropBlock(t, x, y, greenBoard)
    
    if(t==1):
        dropBlock(1, y, 3-x, blueBoard)
    elif(t==2):
        dropBlock(3, y, 3-x, blueBoard)
    elif(t==3):
        dropBlock(2, y, 3-x-1, blueBoard)
    
    greenBoard = checkBoard(greenBoard)
    blueBoard = checkBoard(blueBoard)


print(score, sum(map(sum, greenBoard + blueBoard)), sep = "\n")