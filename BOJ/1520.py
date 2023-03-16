# 완전 탐색으로 풀이 후, 시간초과로 틀림 : 완전 탐색 시 지나온 경로를 생각하지 않아도 됨(수가 줄어들어서)

# DFS, DP 아이디어 생각 못함....
# DFS를 이용한 DP로 문제를 풀었는데, 값을 -1이 아닌 0으로 초기화시 시간초과
# => 끝에 도달하지 못하는 구간(주변이 자신보다 높은 값들만 존재)은 0이라는 초기값으로 나타내지는데,

# TIP)  DP의 초기값을 0이라고 하면, 이런 값들을 참조할 때 계산을 하지 않은 것인지(0), 계산을 했는데 경우의 수가 존재하지 않는지(0) 구분이 안됨. 
#       따라서, 초기값을 -1이라고 하면, 계산을 했는데 경우가 없음(0), 지나가지 않음(-1)를 구분할 수 있어 계산이 줄어든다.


import sys
input = sys.stdin.readline
m, n = map(int, input().split())

sys.setrecursionlimit(100000)

arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

dydx = [[-1,0], [1,0], [0,-1], [0,1]]
dest = [[-1] * (n) for _ in range(m)] # 해당 위치에서 m,n에 도달할 수 있는가


def lazySejun(y, x): # (y,x)에서 끝에 도달할 경우의 수를 의미
    if(dest[y][x] != -1):
        return dest[y][x]
    
    if((y == m-1 and x == n-1)):
        return 1
    
    ans = 0
    for dy, dx in dydx:
        ny = y + dy; nx = x + dx
        if(0 <= ny < m and 0 <= nx < n and arr[ny][nx] < arr[y][x]):
            ans += lazySejun(ny, nx)

    dest[y][x] = ans
    return dest[y][x]

print(lazySejun(0, 0))