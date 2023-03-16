# 단순 구현? => DP 같은데

inst = list(map(int, input().split()))

n = len(inst)

move = [[0,2,2,2,2], [0,1,3,4,3], [0,3,1,3,4], [0,4,3,1,3], [0,3,4,3,1]]


dp = [[[float("INF")] * 5 for _ in range(5)] for _ in range(n + 1)]  # [step][l][r] : 해당 단계에서 l,r에 있을 때 최소의 힘
ans = 0
dp[0][0][0] = 0

for i in range(n):
    next = inst[i]
    for l in range(5): # (l,r)을 순회하면서 해당 위치에서 이동할 수 있는 경우 찾기
        for r in range(5): 
            if(l != next): #오른발을 움직이는데, 왼쪽 발이 해당 위치에 없다면
                dp[i+1][l][next] = min(dp[i+1][l][next], dp[i][l][r] + move[r][next])
            if(r != next):
                dp[i+1][next][r] = min(dp[i+1][next][r], dp[i][l][r] + move[l][next])
    
print(min(list(map(min, dp[n]))))