# dp[3] = (dp[2] - 1) * 2 + 2^1 + 1 = 5
# dp[4] = (dp[3] - 1) * 2 + 2^2 + 1 = 13

a, b = map(int, input().split())

dp = [[0,0]] * 100
dp[1] = [1, 1]

for i in range(2, 70):
    dp[i] = [(dp[i-1][0] - 1) * 2 + 2**(i-2) + 1, dp[i-1][1] * 2]

def calcOne(s):
    ans = 0
    for i in range(len(s)):
        if(s[i] == '1'):
            count = 0
            for j in range(i-1, -1, -1):
                if(s[j] == '1'):
                    count += 1
            ans += dp[len(s)-i][0] + count * dp[len(s)-i][1]

    return ans

print(calcOne(bin(b)[2:]) - calcOne(bin(a-1)[2:]))