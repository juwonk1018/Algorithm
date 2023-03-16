import sys
input = sys.stdin.readline

n = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(n):
    step = list(map(int, input().split()))
    if(i==0):
        max_dp[0] = step[0]; max_dp[1] = step[1]; max_dp[2] = step[2]
        min_dp[0] = step[0]; min_dp[1] = step[1]; min_dp[2] = step[2]
    
    else:
        max_copy = max_dp.copy()
        min_copy = min_dp.copy()

        max_dp[0] = max(max_copy[0] + step[0], max_copy[1] + step[0])
        max_dp[1] = max(max_copy[0] + step[1], max_copy[1] + step[1], max_copy[2] + step[1])
        max_dp[2] = max(max_copy[1] + step[2], max_copy[2] + step[2])

        min_dp[0] = min(min_copy[0] + step[0], min_copy[1] + step[0])
        min_dp[1] = min(min_copy[0] + step[1], min_copy[1] + step[1], min_copy[2] + step[1])
        min_dp[2] = min(min_copy[1] + step[2], min_copy[2] + step[2])
        
print(max(max_dp), min(min_dp))
