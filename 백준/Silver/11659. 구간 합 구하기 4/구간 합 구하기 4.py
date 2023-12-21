import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n):
    dp[i] = dp[i-1] + arr[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j-1] - dp[i-2])