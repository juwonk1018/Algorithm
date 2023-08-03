n = int(input())

dp = [0, 0] + [3] + [0] * (n-2)

for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(i-4, -2, -2):
        dp[i] += dp[j] * 2
    dp[i] += 2

print(dp[n])