# DP? dp[n][3]에서 [p][0]은 p번째 집까지 빨강으로 끝나면서 얻을 수 있는 최소 비용?
# => 문제 해결 X

# N번 집은 N-1번, 1번이랑 같으면 안된다는 조건이 추가
# => #dp[i][j]는 i로 시작해서 j로 끝나는 것을 나타냄

import sys
import copy
input = sys.stdin.readline

n = int(input())

dp = [[float("INF")] *3 for _ in range(3)]
r1, g1, b1 = map(int, input().split())
dp[0][0] = r1; dp[1][1] = g1; dp[2][2] = b1



for i in range(n-1):
    dp_copy = copy.deepcopy(dp)
    dp = [[float("INF")] *3 for _ in range(3)] #코드를 줄이려면 매번 초기화 필요
    r, g, b = map(int, input().split())
    rgb = [r, g, b]

    #아래 코드를 줄인 구문
    for j in range(3):
        for k in range(3):
            for l in range(3):
                if(k != l):
                    dp[j][k] = min(dp[j][k], dp_copy[j][l] + rgb[k])
    
    '''
    dp[0][0] = min(dp_copy[0][1] + r, dp_copy[0][2] + r)
    dp[1][1] = min(dp_copy[1][0] + g, dp_copy[1][2] + g)
    dp[2][2] = min(dp_copy[2][1] + b, dp_copy[2][0] + b)
    dp[0][1] = min(dp_copy[0][0] + g, dp_copy[0][2] + g)
    dp[0][2] = min(dp_copy[0][0] + b, dp_copy[0][1] + b)
    dp[1][0] = min(dp_copy[1][1] + r, dp_copy[1][2] + r)
    dp[1][2] = min(dp_copy[1][0] + b, dp_copy[1][1] + b)
    dp[2][0] = min(dp_copy[2][1] + r, dp_copy[2][2] + r)
    dp[2][1] = min(dp_copy[2][0] + g, dp_copy[2][2] + g)
    '''
    
    if(i == n-2):
        dp[0][0] = dp[1][1] = dp[2][2] = float("INF")
            
print(min(map(min, dp)))