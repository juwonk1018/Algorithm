import sys
import heapq

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]

INF = int(1e9)
dist = [INF] * (v+1)

for _ in range(e):
    input = list(map(int, sys.stdin.readline().split()))
    graph[input[0]].append((input[1],input[2]))


def dijkstra(start):
    dist[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        distance, current = heapq.heappop(q)
        if(dist[current] < distance):
            continue
        
        for edge in graph[current]:
            cost = edge[1] + distance
            if(cost < dist[edge[0]]):
                dist[edge[0]] = cost
                heapq.heappush(q, (cost, edge[0]))

dijkstra(start)

for element in dist[1:]:
    if(element != INF):
        print(element)
    else:
        print("INF")