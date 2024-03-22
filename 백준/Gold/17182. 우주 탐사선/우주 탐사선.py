import heapq
import sys
from itertools import permutations

input = sys.stdin.readline

def dijkstra(startIdx):
    distance = [float("INF")] * n
    distance[startIdx] = 0

    hq = [[0, startIdx]]
    while(hq):
        dist, idx = heapq.heappop(hq)
        if(distance[idx] < dist):
            continue

        for nextIndex in range(n):
            total = dist + cost[idx][nextIndex]
            if(idx != nextIndex and total < distance[nextIndex]):
                distance[nextIndex] = total
                hq.append([total, nextIndex])

    min_cost[startIdx] = distance
    

n, k = map(int, input().split())
answer = float("INF")

cost = []
min_cost = [[] for _ in range(n)]

for _ in range(n):
    cost.append(list(map(int, input().split())))

for i in range(n):
    dijkstra(i)

for p in permutations(list(set([i for i in range(n)]) - set([k])), n-1):
    totalCost, curIdx = 0, k    
    for nextIdx in p:
        totalCost += min_cost[curIdx][nextIdx]
        curIdx = nextIdx

    answer = min(answer, totalCost)
    
print(answer)
