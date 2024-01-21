# 처음에는 배열에서 순서대로 접근해서 비교해 union 편입 -> 예제 4번처럼 역순으로 거슬러 올라가는 경우 탐지 X


from collections import deque
import sys

input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, l, r = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def BFS(i, j, visited, countries):
    total = countries[i][j]
    visited[i][j] = True

    union = set({(i,j)})
    q = deque([[i,j]])

    while(q):
        cx, cy = q.popleft()
        for k in range(4):
            nx = cx+dx[k]
            ny = cy+dy[k]
            if(0 <= nx < n and 0 <= ny < n and l <= abs(countries[nx][ny] - countries[cx][cy]) <= r and visited[nx][ny] == False):
                q.append([nx,ny])
                union.add((nx,ny))
                visited[nx][ny] = True
                total += countries[nx][ny]
    
    result = total//len(union)
    for i, j in union:
        countries[i][j] = result
                

while(True):
    migration = False
    visited = [[False] * n for _ in range(n)]
    nextCountries = [countries[i][:] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if(visited[i][j] == False):
                for k in range(2):
                    ni = i+dx[k]
                    nj = j+dy[k]
                    if(0 <= ni < n and 0 <= nj < n and l <= abs(countries[ni][nj] - countries[i][j]) <= r and visited[ni][nj] == False):
                        BFS(i, j, visited, nextCountries)
                        migration = True
    
    if(migration == False):
        print(ans)
        break

    countries = [nextCountries[i] for i in range(n)]
    ans += 1