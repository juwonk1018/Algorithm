import sys
input = sys.stdin.readline

n, k = map(int, input().split())

chess = []
target = [[[] for _ in range(n)] for _ in range(n)]

dr = [0,0,-1,1]
dc = [1,-1,0,0]

for i in range(n):
    chess.append(list(map(int, input().split())))


pos = [[-1, -1] for _ in range(k)]
for i in range(k):
    r, c, direction = map(int, input().split())
    pos[i] = [r-1, c-1]
    target[r-1][c-1].append([i,direction-1])
    
def gameStart():
    for turn in range(1,1001):
        for i in range(k):
            r, c = pos[i]
            tempStack = []
            
            for j in range(len(target[r][c])):
                cur, direction = target[r][c][j]
                if(i == cur): # i번째 index 뒤에 오는 것은 모두 이동 대상
                    tempStack = target[r][c][j:]
                    target[r][c] = target[r][c][:j]
                    nr, nc = r + dr[direction], c + dc[direction]
                    
                    # 체스판을 벗어나거나, 파란색일 경우에는 방향 변경
                    if (0 <= nr < n and 0 <= nc < n and chess[nr][nc] == 2) or (not(0 <= nr < n) or not(0 <= nc < n)):
                        if(direction % 2 == 0):
                            tempStack[0][1] += 1
                        else:
                            tempStack[0][1] -= 1

                        direction = tempStack[0][1]
                        nr, nc = r + dr[direction], c + dc[direction]
                    
                    if(0 <= nr < n and 0 <= nc < n):
                        
                        if(chess[nr][nc] == 1):
                            tempStack = tempStack[::-1]
                        elif(chess[nr][nc] == 2):
                            nr, nc = r, c
                    else:
                        nr, nc = r, c

                    for l in range(len(tempStack)):
                        pos[tempStack[l][0]] = [nr,nc]
                    target[nr][nc] += tempStack
                    
                    # 4개 이상 쌓였는지 체크
                    if(len(target[nr][nc]) >= 4):
                        return turn

                    break

            
    return -1

print(gameStart())