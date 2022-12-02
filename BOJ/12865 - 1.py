"""
Knapsack은 DP로 푸는 방식 알아두기
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    weight, value = map(int, input().split())
    arr.append([weight, value])

dp = [[0] * (k+1) for _ in range(n)] # dp[i][j] : 최대 무게가 j일 때 i번째 물건까지 담을 경우, 가질 수 있는 최대 가치

for i in range(k+1):
    if(arr[0][0] <= i):
        dp[0][i] = arr[0][1]

for i in range(1, n):
    for j in range(k+1):
        if(arr[i][0] <= j):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - arr[i][0]] + arr[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][k])

"""
내 풀이(BackTracking)
ans = 0

def backpack(cur, weight, value):
    global ans
    if(weight > k):
        return
    else:
        for i in range(cur[-1]+1,n):
            if(i not in cur and weight + arr[i][0] <= k):
                backpack(cur + [i], weight + arr[i][0], value + arr[i][1])
                ans = max(ans, value + arr[i][1])
                
for i in range(n):
    backpack([i], arr[i][0], arr[i][1])
print(ans)
"""