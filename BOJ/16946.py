# 단순 dfs? => 시간초과. visited array를 이용하여, 방문했던 기록을 확인

# 0을 기준으로 DFS를 돌려, 마주치는 1에게 수를 더해줌

# => visited를 이용해, 방문하지 않았다면 방문체크 후 수를 더하고, 마지막으로 만난 1의 위치에 개수를 더함

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
wall = []

dydx = [[0,-1], [0,1], [1,0], [-1,0]]

def DFS(y, x):
    oneNode = set([]) # 0을 순회하면서 1을 마주친 위치, list 사용 시 중복 위치 존재
    queue = deque([[y,x]])
    visitNode = 0
    while(queue):
        cy, cx = queue.popleft()
        if(visited[cy][cx]): #이미 방문하면 스킵( 1% 에서 시간초과 후 추가)
            continue
        
        visitNode += 1
        visited[cy][cx] = True
        for dy, dx in dydx:
            ny = cy+dy; nx = cx+dx 
            if(0 <= ny < n and 0 <= nx < m):
                if(arr[ny][nx] == 0 and visited[ny][nx] == 0):
                    
                    queue.append([ny, nx])
                elif(arr[ny][nx] == 1):
                    oneNode.add((ny,nx))
    
    for y, x in oneNode:
        ans[y][x] += visitNode

for i in range(n):
    arr.append([int(i) for i in input().split()[0]])

ans = [[0] * m for _ in range(n)]

visited = [[False] * (m) for _ in range(n)]
for y in range(n):
    for x in range(m):
        if(arr[y][x] == 0 and visited[y][x] == 0):
            DFS(y,x)
        if(arr[y][x] == 1):
            ans[y][x] += 1 #자기 자신의 위치 추가

for i in range(n):
    for j in range(m):
        print(ans[i][j]%10, end = '')
    print()