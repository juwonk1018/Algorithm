import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())

bombTimer = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(r):
    bombTimer.append([3 if element == '3' else -1 for element in list(input().strip().replace("O", '3').replace(".",'0'))])

def setBomb():
    for i in range(r):
        for j in range(c):
            if(bombTimer[i][j] == -1):
                bombTimer[i][j] = 3
    

def boom():
    for i in range(r):
        for j in range(c):
            if(bombTimer[i][j] == 0):
                bombTimer[i][j] = -1
                for idx in range(4):
                    nr, nc = i + dx[idx], j + dy[idx]
                    if(0 <= nr < r and 0 <= nc < c and bombTimer[nr][nc] != 0):
                        bombTimer[nr][nc] = -1
                
for t in range(1, min(n+1,6)):
    for i in range(r):
        for j in range(c):
            if(bombTimer[i][j] > 0):
                bombTimer[i][j] -= 1

    if(t == 1):
        continue

    if(t % 2 == 0):
        setBomb()
        evenTimer = [bombTimer[i][:] for i in range(r)]
        continue
    
    boom()
    if(t == 3):
        timer1 = [bombTimer[i][:] for i in range(r)]
    
    if(t == 5):
        timer2 = [bombTimer[i][:] for i in range(r)]



if(n > 1 and n % 4 == 1):
    bombTimer = [timer2[i][:] for i in range(r)]
elif(n > 1 and n % 4 == 3):
    bombTimer = [timer1[i][:] for i in range(r)]
elif(n > 1 and n % 2 == 0):
    bombTimer = [evenTimer[i][:] for i in range(r)]

for i in range(r):
    for j in range(c):
        if(bombTimer[i][j] > 0):
            print("O", end = "")
        else:
            print(".", end = "")
    print()