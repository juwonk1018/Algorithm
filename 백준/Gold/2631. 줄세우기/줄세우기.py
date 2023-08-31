# 가장 큰 오름차순 수열의 크기를 이용

import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if(arr[j] < arr[i]):
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))