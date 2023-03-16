# 필요한 메모리를 충족하기 위해 앱을 비활성화하는 최소 비용
# = 목표 메모리 이상의 범위에서 특정 앱을 선택해 비용 최소화
# = DP, knapsack.

# 2-d array로 dp[index][cost]로 dp[i][j] = max(memory + dp[i-1][j-cost], dp[i-1][j])로도 구현이 가능
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

totalCost = [-1] * 10001 #해당 비용을 사용해서 지울 수 있는 최대 메모리

for i in range(n):
    newTotalCost = totalCost.copy()

    newTotalCost[cost[i]] = max(totalCost[cost[i]], memory[i])
    
    for j in range(len(totalCost)):
        if(totalCost[j] != -1):
            newTotalCost[j + cost[i]] = max(totalCost[j + cost[i]], totalCost[j] + memory[i])
    
    totalCost = newTotalCost.copy()

ans = float("INF")
for i in range(10001):
    if(totalCost[i] >= m):
        ans = min(ans, i)
print(ans)