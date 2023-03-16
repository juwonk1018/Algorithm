# 가장자리에 '.'을 추가하게 되면, DFS(0,0)만으로도 입구 찾기 가능

import sys
input = sys.stdin.readline

n = int(input())

def checkKey(door):
    for alphabet in key:
        if(door.lower() == alphabet):
            return True
    return False

def DFS(y, x):
    cnt = 0
    global key

    q = [[y,x]]
    while q:
        cy, cx = q.pop()

        
        if(visited[cy][cx]):
            continue

        visited[cy][cx] = True

        if(maps[cy][cx] == '.'): # 빈 공간
            pass
        elif(maps[cy][cx] == '$'): # 문서
            cnt +=1
        elif('A' <= maps[cy][cx] <= 'Z'): #문을 마주칠 때
            if(checkKey(maps[cy][cx]) == False): #문을 열지 못한다면
                doorPos.append([maps[cy][cx], cy,cx]) #글자, y, x 위치를 저장
                continue
        elif('a' <= maps[cy][cx] <= 'z'): #열쇠 마주칠 때
            key += maps[cy][cx]
            for letter, y, x in doorPos:
                if(checkKey(letter)): #열쇠가 만족하면 방문을 하지 않은 것으로 처리하고 해당 위치를 queue에 삽입
                    visited[y][x] = 0
                    q.append([y,x])
            


        for dy, dx in dydx:
            ny, nx = cy+dy, cx+dx
            if(0 <= ny < h and 0 <= nx < w and visited[ny][nx] == False and maps[ny][nx] != '*'):
                q.append([ny,nx])
    return cnt

for _ in range(n):
    h, w = map(int, input().split())

    maps = []
    for _ in range(h):
        maps.append(input().split()[0])

    key = input().split()[0]
    if(key == '0'):
        key = ''

    dydx = [[0,1],[0,-1],[1,0],[-1,0]]

            
    ans = 0
    doorPos = []
    visited = [[False] * w for _ in range(h)]

    # 들어갈 수 있는 가장자리 벽 찾기
    for i in range(h):
        for j in range(w):
            if(i == 0 or i == h-1 or j == 0 or j == w-1):
                if(maps[i][j] != '*'):
                    ans += DFS(i, j) # 빈 공간에서 DFS
    print(ans)