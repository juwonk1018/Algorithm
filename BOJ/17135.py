# 한 archer가 동시에 같은 적을 쏠 수 있다는 조건을 지나쳐서 틀렸었음(문제 잘 읽기)

from itertools import combinations
import sys
input = sys.stdin.readline

n, m, d = map(int, input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

grid.append([0] * m) # 성의 위치

def searchEnemy(grid, y, x, distance):
    result = [-100, -100]
    for i in range(y-distance, y):
        for j in range(x-distance, x+distance+1):
            if(0 <= i < n and 0<= j < m and grid[i][j] == 1 and abs(i-y) + abs(j-x) <= d):
                cal = abs(y-result[0]) + abs(x-result[1]) - (abs(i-y) + abs(j-x))
                if(cal > 0): # 격차가 줄어들었다면
                    result = [i, j]
                elif(cal == 0 and j < result[1]): #격차가 똑같다면 가장 왼쪽에 있는 것을 선택
                    result = [i, j]
                    
    return result             

ans = 0
totalEnemy = sum([sum(grid[i][:]) for i in range(n)])

for archerPos in combinations(range(m), 3):
    res = 0
    enemyNumber = totalEnemy; grid_copy = [grid[i][:] for i in range(n+1)]
    while(enemyNumber != 0): 
        removeArcher = set()
        for pos in archerPos: # 궁수의 위치마다 적을 찾고 제거
            enemyPos = searchEnemy(grid_copy, n, pos, d)
            if(enemyPos != [-100,-100]): # 찾았다면 제거
                removeArcher.add((enemyPos[0], enemyPos[1]))

        enemyNumber -= len(removeArcher)
        res += len(removeArcher)
        for pos in removeArcher:
            grid_copy[pos[0]][pos[1]] = 0
        
        for i in range(n-1, -1, -1): # 적을 한칸씩 아래로 이동
            for j in range(m):
                if(grid_copy[i][j] == 1):
                    if(i == n-1): 
                        enemyNumber -= 1
                    grid_copy[i][j] = 0
                    grid_copy[i+1][j] = 1
        
    ans = max(ans, res)  

print(ans)