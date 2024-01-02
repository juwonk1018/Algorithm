import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0,0,0,0]]

dx = [1,1,1]
dy = [-1,0,1]

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[[0] * 3 for _ in range(m)]] + [[[float("INF"),float("INF"),float("INF")] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        for k in range(3):
            for l in range(3):
                if(k != l and 0 <= j+dy[l] < m):
                    dp[i+dx[l]][j+dy[l]][l] = min(dp[i+dx[l]][j+dy[l]][l], dp[i][j][k] + arr[i+dx[l]][j+dy[l]])

print(min(list(map(min,dp[-1]))))