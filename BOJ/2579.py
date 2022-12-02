import sys
n = int(sys.stdin.readline())
stair = []
for _ in range(n):
    stair.append(int(sys.stdin.readline().strip()))

noNextStair = stair.copy()

for i in range(1,n):
    noNextStair[i] = stair[i-1] + stair[i]
    if(i>1):
        stair[i] = max(noNextStair[i-2] + stair[i], stair[i-2] + stair[i])
print(max(noNextStair[n-1], stair[n-1]))

#dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])로도 가능 