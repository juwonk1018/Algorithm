# DP를 모두 구해두고, partialSum(start, i) * 2 + partialSum(i+1, end)와 같은 형식은
# 파일을 합칠 때 (start, end) 까지의 크기를 의미하는 것이 아니라 [start, i] 까지의 최소비용을 한 번 더 더하는 것. (혼동주의)

# 재귀로 못푸는 문제..? => 전부 시간초과

# 대각선으로 DP를 해결해야 문제가 빨리 풀림.... <- 새롭게 배운 것
# min을 최소화, pypy3 로만 통과

import sys
input = sys.stdin.readline

def sol():
    t = int(input())


    for _ in range(t):

        k = int(input())
        arr = list(map(int, input().split()))

        s = [0] * (k+1)
        for i in range(k):
            s[i] = s[i-1] + arr[i]
        
        dp = [[0]*k for i in range(k)]    
        
        for i in range(1, k):
            for j in range(0, k-i): #j를 기준으로 i만큼 왼,오른쪽 가기
                dp[j][j+i] = min([dp[j][j+l] + dp[j+l+1][j+i] for l in range(i)]) + s[j+i] - s[j-1]
                
        print(dp[0][k-1])
sol()