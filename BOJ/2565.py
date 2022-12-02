import sys
n = int(sys.stdin.readline())
pole = []
for _ in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    pole.append(input)

pole.sort()

dp = [1] * n

for i in range(n):
    for j in range(i):
        if(pole[i][1] > pole[j][1]):
            dp[i] = max(dp[j] + 1, dp[i])
        
print(n - max(dp))


"""
sol = 1

def dp(pole, cur):
    global sol
    prev = cur[-1][1]
    for i in range(0,len(pole)):
        if(prev < pole[i][1] and pole[i][0] > cur[-1][0]):

            dp(pole,cur + [pole[i]])
        else:
            pass
        
    if(sol < len(cur)):
        sol = len(cur)

for i in range(len(pole)):
    dp(pole, [pole[i]])

print(n - sol)
"""

# 최장증가수열(LIS)가 답.. 나는 element가 1개인것부터 조건에 맞는 2,3개씩 쌓았지만 시간초과