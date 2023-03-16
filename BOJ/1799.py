# n-queen과 같은 backtracking? => 시간복잡도 초과
# 대각선만 고려하여, 각 대각선에서 하나씩 가능한 것을 선택해 DFS
# 흰 칸과 검은 칸은 서로 영향을 줄 수 없으므로 분리해서 계산해도 된다. => 크기가 N/2 * N/2로 줄어든다.
# 2^100 => 2^25로 줄어든다.

# 풀이 다듬기..


import sys

n = int(input())

sys.setrecursionlimit(1000000)

chess = []
for i in range(n):
    chess.append(list(map(int, input().split())))

ans = 0
move = [[1,1], [1,-1], [-1,1], [-1,-1]]

i=0; j=0

def bishop(chess, y, x, cnt):
    global partialSum
    num = 0

    chess_copy = [chess[i][:] for i in range(n)]
    if(chess[y][x] == 1): #비숍을 둘 수 있으면 두고 갈 수 있는 위치 파악
        num = 1    
        chess_copy[y][x] = 0 #비숍을 해당 위치에 두고
        partialSum = max(partialSum, cnt+1)
        for dy, dx in move: #비숍이 갈 수 있는 곳을 0으로 두기
            for k in range(n):
                if(0<= y + dy*k < n and 0 <= x + dx*k < n):
                    chess_copy[y+dy*k][x+dx*k] = 0
    
    #이후에 다음 위치에 갈 수 있는지 체크

    checked = False
    if(x < n-2 and y == 0):
        for i in range(-n, n):
            if(0 <= y+i < n and 0 <= x+2-i < n and chess_copy[y+i][x+2-i] == 1):
                checked = True
                bishop(chess_copy, y+i, x+2-i, cnt+num)

    elif(x == n-2 and y == 0):
        for i in range(-n, n):
            if(0 <= y+1+i < n and 0 <= x+1-i < n and chess_copy[y+1+i][x+1-i] == 1):
                checked = True 
                bishop(chess_copy, y+1+i, x+1-i, cnt+num)
                
    elif(y != n):
        for i in range(-n, n):
            if(0 <= y+2+i < n and 0 <= x-i < n and chess_copy[y+2+i][x-i] == 1):
                checked = True 
                bishop(chess_copy, y+2+i, x-i, cnt+num)
                 

    if(not(checked)): # 다음 라인에 둘 비숍을 찾지 못함
        if(0 <= x+2 < n):
            bishop(chess_copy, y, x+2, cnt + num)
        elif(x == n-2 and y == 0):
            bishop(chess_copy, y+1, x+1, cnt + num)
        elif(0 <= y+2 < n):
            bishop(chess_copy, y+2, x, cnt + num)
     

partialSum = 0
bishop(chess, 0, 0, 0)
ans += partialSum

if(n>=2): #둘 중에 하나만 선택해서 실행하면 틀림...
    num2 = 0

    for i in range(2):
        partialSum = 0
        bishop(chess, i,1-i, 0)
        num2 = max(num2, partialSum)
    
    ans += num2

print(ans)
