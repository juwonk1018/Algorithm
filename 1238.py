import sys
import heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())

road = [[] for _ in range(n+1)]
for _ in range(m):
    src, dst, cost = map(int, input().split())
    road[src].append([dst,cost])


#X에서 각 마을까지 걸리는 최소비용
toHome = [float("INF")] * (n+1)
queue = []
heapq.heappush(queue, [0,x])
toHome[x] = 0

while(queue):
    total, cur = heapq.heappop(queue)
    if(total > toHome[cur]):
        continue

    for dst, cost in road[cur]:
        if(toHome[dst] > total + cost):
            toHome[dst] = total + cost
            heapq.heappush(queue, [total + cost, dst])
        
ans = 0

#각 마을에서 X까지 걸리는 최소비용
for i in range(1,n+1):
    toX = [float("INF")] * (n+1)
    queue = []
    queue.append([0,i])
    toX[i] = 0

    while(queue):
        total, cur = heapq.heappop(queue)
        if(total > toX[cur]):
            continue
        for dst, cost in road[cur]:
            if(toX[dst] > total + cost):
                toX[dst] = total + cost
                heapq.heappush(queue, [total + cost, dst])

    ans = max(ans, toX[x]+toHome[i])

print(ans)

#### 간선을 모두 뒤집고, X에서 다익스트라를 사용하면 모든 node에서 X로 가는 최소 비용이 구해짐 