# BFS로 하나씩 탐색하지말고, 오른쪽을 다 탐색하고 이후로 아래로 순차적으로 탐색

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[[0] * (n) for _ in range(n)] for _ in range(3)]
# 0은 가로, 1은 대각선, 2는 세로

dp[0][0][1] = 1


for y in range(n):
    for x in range(n):
        if(0 <= y < n and 0 <= x+1 < n and arr[y][x+1] == 0):
            dp[0][y][x+1] += dp[0][y][x]
            dp[0][y][x+1] += dp[1][y][x]
        if(0 <= y < n and 0 <=  y+1 < n and 0 <= x < n and 0 <= x+1 < n):
            if(arr[y+1][x] == 0 and arr[y][x+1] == 0 and arr[y+1][x+1] == 0):
                dp[1][y+1][x+1] += dp[0][y][x] + dp[1][y][x] + dp[2][y][x] 
        if(0 <= y+1 < n and 0<= x < n and arr[y+1][x] == 0):
            dp[2][y+1][x] += dp[2][y][x]
            dp[2][y+1][x] += dp[1][y][x]
    
print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])