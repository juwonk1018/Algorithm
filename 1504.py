import sys
import heapq
from collections import deque

INF = int(1e9)
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    line = list(map(int, sys.stdin.readline().split()))
    graph[line[0]].append((line[1],line[2]))
    graph[line[1]].append((line[0],line[2]))

v1, v2 = map(int, input().split())

# heapq 를 사용하면 시간이 많이 줄어듦.
def dijkstra(start):
    q = []
    dist = [INF] * (v+1)
    dist[start] = 0
        
    heapq.heappush(q, (0,start))
    
    while(q):
        distance, cur = heapq.heappop(q)
        if(dist[cur] < distance):
            continue

        for element in graph[cur]:
            cost = distance + element[1]

            if(dist[element[0]] > cost):
                dist[element[0]] = cost
                heapq.heappush(q, (cost, element[0]))

    return dist

start_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = start_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = start_distance[v2] + v2_distance[v1] + v1_distance[v]
result = min(v1_path, v2_path)
print(result if result < INF else -1)

"""
ans = 0
def dijkstra(start, end):
    visited = [False] * (v+1)
    dist = [INF] * (v+1)
    queue = deque()
    queue.append(start)
    dist[start] = 0
    while(queue):
        cur = queue.popleft()
        if cur != end:
            visited[cur] = True
            for element in graph[cur]:
                if(dist[element[0]] == INF or dist[element[0]] > dist[cur] + element[1]):
                    queue.append(element[0])
                    dist[element[0]] = min(dist[cur] + element[1], dist[element[0]])
    
    return dist[end]


b1 = dijkstra(1,v2)
b2 = dijkstra(v2,v1)
b3 = dijkstra(v1,v)

a1 = dijkstra(1,v1)
a2 = dijkstra(v1,v2)
a3 = dijkstra(v2,v)

if(min(b1+b2+b3, a1+a2+a3) == b1+b2+b3):
    if(max(b1,b2,b3) == INF):
        print(-1)
    else:
        print(b1+b2+b3)

elif(min(b1+b2+b3, a1+a2+a3) == a1+a2+a3):
    if(max(a1,a2,a3) == INF):
        print(-1)
    else:
        print(a1+a2+a3)

"""

