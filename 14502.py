import copy
from collections import deque
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dxdy = [[-1,0],[0,1],[1,0],[0,-1]]

def bfs(arr2):
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = arr2[i][j]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if(arr[i][j] == 2):
                queue.append([i,j])
    while(queue):
        i, j = queue.popleft()
        for dx, dy in dxdy:
            if(0<= i+dx < n and 0<= j+dy < m):
                if(arr[i+dx][j+dy] == 0):
                    arr[i+dx][j+dy] = 2
                    queue.append([i+dx,j+dy])
        
    
    cnt = 0
    for i in range(n):
        cnt += arr[i].count(0)
    return cnt
            
ans = 0

def wall(count, arr):
    global ans
    if(count == 3):
        ans = max(ans, bfs(arr))
        
    else:
        for i in range(n):
            for j in range(m):
                if(arr[i][j] == 0):
                    arr[i][j] = 1
                    wall(count+1, arr)
                    arr[i][j] = 0

    return ans

print(wall(0, arr))
