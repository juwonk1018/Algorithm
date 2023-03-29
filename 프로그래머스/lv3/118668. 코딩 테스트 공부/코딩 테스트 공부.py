def solution(alp, cop, problems):
    
    # 최대 수치 찾기
    max_alp, max_cop = max([alp] + [x[0] for x in problems]), max([cop] + [x[1] for x in problems]) 
    
    dp = [[float("INF") for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    
    if(alp >= max_alp and cop >= max_cop):
        return 0
    
    dp[alp][cop] = 0
    
    for i in range(alp+cop, max_alp + max_cop + 1): # i는 counter
        for j in range(alp, i+1): # j = alp, i-j = cop
            if(alp <= j <= max_alp and cop <= i-j <= max_cop):
                na = min(max_alp, j+1)
                nc = min(max_cop, i-j+1)
                
                dp[na][i-j] = min(dp[j][i-j] + 1, dp[na][i-j]) # 이 과정은 problems에 [0,0,1,0,1] 추가해서 요약 가능
                dp[j][nc] = min(dp[j][i-j] + 1, dp[j][nc])            

                for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                    if(alp_req <= j and cop_req <= i-j and alp_rwd + cop_rwd > cost):
                        na, nc = min(max_alp, j+alp_rwd), min(max_cop, i-j+cop_rwd)
                        dp[na][nc] = min(dp[na][nc], dp[j][i-j] + cost)

    return dp[max_alp][max_cop]
    
    