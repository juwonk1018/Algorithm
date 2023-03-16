# 주사위 굴리기 문제.
# 내가 푼 것처럼 위, 앞, 옆이 뭔지 현재 상태를 나타낼 수도 있지만,
# dice[0], dice[1] ... dice[5] =  dice[3], dice[1], .... dice[2] 처럼 동서남북으로 굴렸을 때 바뀌는 위치를 기재할 수도 있음
# => dice[0]이 제일 위를 의미
import sys
input = sys.stdin.readline

dice = [0, 0, 0, 0, 0, 0, 0]

# [i][j]는 i 숫자에서 j 방향으로 이동시 윗면의 숫자를 의미

n, m, x, y, k = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))


cur = 1; cur2 = 3; cur3 = 5 # cur은 윗 면, cur2는 동쪽, cur3는 남쪽

command = list(map(int, input().split()))
for i in range(k):
    isMoved = False
    if(command[i] == 1 and y != m-1): #끝이 아니라면 동쪽으로 이동
        cur, cur2 = 7 - cur2, cur
        y += 1; isMoved = True
    elif(command[i] == 2 and y != 0): #서
        cur, cur2 = cur2, 7 - cur
        y -= 1; isMoved = True
    elif(command[i] == 3 and x != 0): #북
        cur, cur3 = cur3, 7 - cur
        x -= 1; isMoved = True
    elif(command[i] == 4 and x != n-1): #남
        cur, cur3 = 7 - cur3, cur
        x += 1; isMoved = True
    
    if(isMoved):
        if(maps[x][y] == 0): #주사위가 0이면 바닥의 수를 복사
            maps[x][y] = dice[7-cur]
        else:
            dice[7-cur] = maps[x][y]
            maps[x][y] = 0
        print(dice[cur])
