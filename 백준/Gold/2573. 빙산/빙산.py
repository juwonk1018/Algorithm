from collections import deque
import sys

input = sys.stdin.readline


def afterOneYear():
    for i in range(n):
        for j in range(m):
            if(glacier[i][j]):
                glacierDict = BFS(i, j)
                lossNumber = 0
                for ci,cj in glacierDict:
                    glacier[ci][cj] = max(0, glacier[ci][cj] - glacierDict[(ci,cj)])
                    if(glacier[ci][cj] == 0):
                        lossNumber += 1
                afterGlacierDict = checkGlacier()
                if(len(glacierDict) - lossNumber != len(afterGlacierDict) or len(afterGlacierDict) == 0):
                    return False
                else:
                    return True

    return False


def checkGlacier():
    for ii in range(n):
        for jj in range(m):
            if(glacier[ii][jj]):
                return BFS(ii, jj)
    return dict()

def BFS(i, j):
    visited = dict()
    q = deque([[i, j]])
    while(q):
        ci, cj = q.popleft()
        glacierLoss = 0
        for i in range(4):
            ni, nj = ci + dx[i], cj + dy[i]
            if(0 <= ni < n and 0 <= nj < m):
                if(glacier[ni][nj] == 0):
                    glacierLoss += 1
                else:
                    if((ni,nj) not in visited):
                        visited[(ni,nj)] = 0
                        q.append([ni,nj])

        visited[(ci,cj)] = glacierLoss

    return visited

n, m = map(int, input().split())

glacier = []
dx = [1,0,0,-1]
dy = [0,1,-1,0]

for i in range(n):
    glacier.append(list(map(int, input().split())))

ans = 0

result = True
while(result):
    ans += 1
    result = afterOneYear()


print(ans if sum(list(map(sum, glacier))) != 0 else 0)