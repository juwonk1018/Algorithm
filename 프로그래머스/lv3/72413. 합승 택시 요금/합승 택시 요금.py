from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    for st, ed, co in fares:
        dic[st].append((co, ed))
        dic[ed].append((co, st))
    ans = []
    for i in range(1, n+1):
        Q = [(0, i)]
        dp = [float('inf')] * (n+1)
        dp[i] = 0
        while Q:
            co, des = heapq.heappop(Q)
            if(dp[des] < co):
                continue
                
            for cost, destination in dic[des]:
                dp[destination] = min(cost + co, dp[destination])
                heapq.heappush(Q, (cost + co, destination))
        ans.append(dp[a] + dp[b] + dp[s])

    return min(ans)