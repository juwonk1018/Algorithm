def solution(sticker):
    n = len(sticker)
    dp = [[sticker[0], 0]] + [[0, 0] for _ in range(n)] # dp[i][0]은 idx=0 포함, 1은 idx=0 포함 X.
    
    for i in range(1, n):
        if(i==1):
            dp[i] = [sticker[0], sticker[i]]
        elif(i==2):
            dp[i] = [dp[0][0] + sticker[i], dp[0][1] + sticker[i]]
        elif(i != n-1):
            dp[i][0] = max(dp[i-2][0] + sticker[i], dp[i-3][0] + sticker[i])
            dp[i][1] = max(dp[i-2][1] + sticker[i], dp[i-3][1] + sticker[i])
        elif(i == n-1): # 마지막 index
            dp[i][1] = max(dp[i-2][1] + sticker[i], dp[i-3][1] + sticker[i])
            
    
    answer = max(list(map(max, dp)))
    
    
        
    return answer