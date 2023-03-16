# 가장자리를 BFS 돌려서 외부 공기가 무엇인지 파악 후 외부공기를 -1로 두기.
# 치즈가 사라진 자리를 -1로 두고(외부 공기랑 반드시 이어지므로), 주변에 내부공기(0)이 있다면 이를 bfs

# bfs를 매번 돌려서 외부 공기를 확인하는 것도 방법이다.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
cheese = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    cheese += sum(arr[i])


dydx = [[1, 0], [-1, 0], [0, 1], [0,-1]]

def bfs(arr, y, x):
    queue = [[y,x]]
    arr[y][x] = -1
    while(queue): #외부 공기를 -1로 표시
        y, x = queue.pop()
        for i in range(4):
            dy, dx = dydx[i]
            ny, nx = y + dy, x + dx
            if(0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0):
                arr[ny][nx] = -1
                queue.append([ny,nx])


bfs(arr, 0, 0) # 외부 공기 파악

ans = 0
while(cheese):
    arr_copy = [arr[i][:] for i in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if(arr[i][j] == 1):
                cnt = 0
                for k in range(4):
                    dy, dx = dydx[k]
                    if(arr[i + dy][j + dx] == -1):
                        cnt += 1
                if(cnt >=2):
                    arr_copy[i][j] = -1
                    for k in range(4):
                        dy, dx = dydx[k]
                        if(arr[i+dy][j+dx] == 0):
                            bfs(arr_copy, i+dy, j+dx) #외부랑 이어지는 공기 체크
                    cheese -= 1
    arr = [arr_copy[i][:] for i in range(n)]
    ans += 1

print(ans)
