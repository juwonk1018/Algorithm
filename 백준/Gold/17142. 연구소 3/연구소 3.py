import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

lab = []
virus = []
vacantSpace = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = -1

def calculateTime(comb):
    global ans
    q = []
    num = len(virus) # 초기에 바이러스가 차지하는 공간

    for i in comb:
        q.append([virus[i][0], virus[i][1]])
        labCopy[virus[i][0]][virus[i][1]] = 3

    cnt = 0
    while(q):   
        nq = []     

        if(num == vacantSpace):
            break
        
        for i in range(len(q)):
            cx, cy = q[i]
            for j in range(4):
                nx, ny = cx + dx[j], cy + dy[j]
                if(0 <= nx < n and 0 <= ny < n and labCopy[nx][ny] == 0):
                    labCopy[nx][ny] = 3 # 바이러스가 퍼진 구역 처리 
                    num += 1 # 바이러스가 차지하는 공간 크기
                    nq.append([nx, ny])
                elif(0 <= nx < n and 0 <= ny < n and labCopy[nx][ny] == 2):
                    labCopy[nx][ny] = 3 # 바이러스가 퍼진 구역 처리 
                    nq.append([nx, ny])

        if(nq):
            cnt += 1
            q = nq + [] # queue를 cnt + 1 상태로 교체
        else:
            q = []
        
    if(num == vacantSpace):
        if(ans == -1):
            ans = cnt
        else:
            ans = min(ans, cnt)

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if(line[j] == 2):
            virus.append([i,j])
            vacantSpace += 1
        elif(line[j] == 0):
            vacantSpace += 1
    lab.append(line)

for comb in combinations([i for i in range(len(virus))], m):
    labCopy = [lab[i][:] for i in range(n)]
    calculateTime(comb)

print(ans)