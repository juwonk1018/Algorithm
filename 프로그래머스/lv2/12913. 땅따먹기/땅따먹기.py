def solution(land):
    dp = [0,0,0,0]
    for a,b,c,d in land:
        n_dp = [0,0,0,0]
        
        n_dp[0] = max(dp[1] + a, dp[2] + a, dp[3] + a)
        n_dp[1] = max(dp[0] + b, dp[2] + b, dp[3] + b)
        n_dp[2] = max(dp[0] + c, dp[1] + c, dp[3] + c)
        n_dp[3] = max(dp[0] + d, dp[1] + d, dp[2] + d)
        
        dp = n_dp
    return max(dp)