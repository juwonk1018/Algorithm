import sys

input = sys.stdin.readline
n, m, h = map(int, input().split())

def checkLadder():
    for i in range(1, n+1):
        cur = i

        for height in range(1, h+1):
            if(ladderPosition[height][cur]):
                cur += 1
            elif(cur > 0 and ladderPosition[height][cur-1]):
                cur -= 1

        if(cur != i):
            return False
    
    return True

def putLadder(num, x, y):
    global answer
    if(checkLadder()):
        answer = min(answer, num)
        return
 
    if(num <= min(2, answer)): # -> 이 조건을 line 32의 맨 뒤에 추가해서 num == 3일 때에도 n*(h+1) cycle을 돌아서 느렸던 것.
        for i in range(y, n):
            if(i == y):
                for j in range(y, h+1):
                    if(ladderPosition[j][i] == 0 and ladderPosition[j][i-1] == 0 and ladderPosition[j][i+1] == 0):
                        ladderPosition[j][i] = 1
                        putLadder(num + 1, j, i)
                        ladderPosition[j][i] = 0
            else:
                for j in range(1, h+1):
                    if(ladderPosition[j][i] == 0 and ladderPosition[j][i-1] == 0 and ladderPosition[j][i+1] == 0):
                        ladderPosition[j][i] = 1
                        putLadder(num + 1, j, i)
                        ladderPosition[j][i] = 0
    
ladderPosition = [[0] * (n+1) for _ in range(h+1)]

answer = float("INF")
for _ in range(m):
    a, b = map(int, input().split())
    ladderPosition[a][b] = 1

if(m==0):
    answer = 0
else:
    putLadder(0, 1, 1)

print(answer if answer != float("INF") else -1)