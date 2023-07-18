import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
dxdy = [[1,0],[-1,0],[0,1],[0,-1]]
ans = float("INF")

arr = []
island = []

def BFS(arr, i, j):
    islandList = []

    q = deque([[i,j]])
    arr[i][j] = 0

    while(q):
        cx, cy = q.popleft()
        islandList.append([cx,cy])
        

        for dx, dy in dxdy:
            nx, ny = cx + dx, cy + dy
            if(0 <=nx < n and 0 <= ny < m and arr[nx][ny]):
                q.append([nx,ny])
                arr[nx][ny] = 0
    
    return islandList

def calcDist(i1, i2):
    dist = float("INF")
    for x1, y1 in i1:
        for x2, y2 in i2:
            if(x1==x2):
                for i in range(min(y1,y2)+1, max(y1,y2)):
                    if(arr[x1][i] == 1):
                        break
                else:
                    if(abs(y1-y2) - 1 > 1):
                        dist = min(dist, abs(y1-y2) - 1)
            elif(y1==y2):
                for i in range(min(x1,x2)+1, max(x1,x2)):
                    if(arr[i][y1] == 1):
                        break
                else:
                    if(abs(x1-x2) - 1 > 1):
                        dist = min(dist, abs(x1-x2) - 1)
    
    if(dist == float("INF") or dist < 2):
        dist = -1
    
    return dist


def find(x):
    if(x != parent[x]):
        parent[x] = find(parent[x])
    return parent[x]


def union(c1, c2):
    p1 = find(c1)
    p2 = find(c2)

    if(p1 < p2):
        parent[p2] = p1
    else:
        parent[p1] = p2


def putBridge(a, connection, total):
    
    
    global ans

    start = a[-1]

    for i in range(len(island)):
        if(parent[i] != parent[0]):
            break
    else:
        ans = min(ans, total)

    for i in range(len(connection)):
        dest, dist = connection[i]
        p1, p2 = find(dest), find(start)
        if(p1 != p2):
            temp1, temp2 = parent[start], parent[dest]
            union(start, dest)
            putBridge(a + [dest], connection[:i] + connection[i+1:] + islandConnection[dest], total + dist)
            parent[start], parent[dest] = temp1, temp2

    
ans = float("INF")

for _ in range(n):
    arr.append(list(map(int, input().split())))

arrCopy = [arr[i][:] for i in range(n)]

for i in range(n):
    for j in range(m):
        if(arrCopy[i][j]):
            island.append(BFS(arrCopy, i, j))


islandConnection = [[] for _ in range(len(island))]

for i in range(len(island)):
    for j in range(i+1, len(island)):
        dist = calcDist(island[i], island[j])
        if(dist > 1):
            islandConnection[i].append([j, dist])
            islandConnection[j].append([i, dist])

parent = [i for i in range(len(island))]

putBridge([0], islandConnection[0], 0)

print(ans if ans != float("INF") else -1)