def solution(N, number):
    dp = [float("INF")] * 100001
    cur = set()
    for i in range(1, 6):
        num = int(str(N) * i)
        cur.add(num)
        dp[num] = i
    
    for _ in range(3):
        curList = list(cur)
        for num in curList:
            for num2 in curList:
                nextNumber = [num + num2, abs(num - num2), num * num2, num // num2, num2 // num]
                for nxt in nextNumber:
                    if(0 < nxt <= 100000):
                        dp[nxt] = min(dp[nxt], dp[num] + dp[num2])
                        if(dp[nxt] <= 8):
                            cur.add(nxt)
    if(dp[number] > 8):
        return -1

    return dp[number]