import sys, heapq
input = sys.stdin.readline

def dijkstra(l, idx):
    
    cost = [-1] * (l+1)
    cost[idx] = 0
    hq = [[0, idx]]
    while(hq):
        time, cur = heapq.heappop(hq)
        if(cost[cur] != -1 and cost[cur] < time): # 방문한 적 있으며 작은 경우
            continue
        
        cost[cur] = time

        for infectSecond, nextComputer in dependency[cur]:
            nextTime = time + infectSecond
            if(cost[nextComputer] == -1):
                heapq.heappush(hq, [nextTime, nextComputer])

    return cost


t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    dependency = [[] for _ in range(n+1)]

    for _ in range(d):
        a,b,s = map(int, input().split())
        dependency[b].append([s,a])

    cost = dijkstra(n, c)

    print(n - cost.count(-1) + 1, max(cost))
