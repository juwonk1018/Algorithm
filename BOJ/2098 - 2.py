import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
MAX = sys.maxsize
dp = [[-1] * (1<<n) for _ in range(n)]

# bitmask : 1101은 4,3,1번째 city의 방문을 의미

def TSP(cur, visited):
    
    if(dp[cur][visited] != -1):
        return dp[cur][visited]

    if(visited == (1 << n) - 1): #bitmasking이 1111... 로 모두 순회시
        if(cost[cur][0]):
            return cost[cur][0]
            #ans = min(ans, dp[cur][visited] + cost[cur][0]) 
        else:
            return MAX
    
    ret = MAX
    for i in range(1, n):
        if(cost[cur][i] != 0 and (visited & (1 << i)) == 0): # 경로가 존재하고, 방문한 적이 없다면
            ret = min(ret, cost[cur][i] + TSP(i, visited | (1 << i)))
    
    dp[cur][visited] = ret

    return dp[cur][visited]

print(TSP(0, 1))

# BFS로 풀이
# +) DP, bitmasking 까지 같이 들어있는 문제...

# bottom-up보다 top-down이 빠름
# top-down 방식 구현하는 법 다시 보기.. 다른 코드 참고해서 구현함

# 58%에서 시간초과.. -> dp를 inf가 아닌 0으로 설정하니 맞음..? overflow와 관련된 시간초과 문제인가?

# f = [0], f[0] = min(f[0], float("inf") + 323)
# f = [inf], f[0] = min(f[0], float("inf") + 323) 를 100만회 실행 후 비교해보니 전자가 빠름..
# inf와 inf를 비교해서 느릴수도..?