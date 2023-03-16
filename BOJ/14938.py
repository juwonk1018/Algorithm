import sys
import heapq

input = sys.stdin.readline

# 1) 다익스트라 알고리즘 풀이
def dijkstra(start):
    distance = [float("INF")] * (n+1)
    distance[start] = 0

    q = [[distance[start], start]]

    while q:
        total, cur = heapq.heappop(q)

        if(total > distance[cur]): # queue에 수가 쌓이면서 이전에는 최소값이라 판단해 넣어진 것도 최소값이 아닐 수 있음
            continue
        for dst, length in cost[cur]:
            if(distance[dst] > total + length):
                distance[dst] = total + length
                heapq.heappush(q, [distance[dst], dst])

    return distance


n, m, r = map(int, input().split())
item = list(map(int, input().split()))
cost = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    cost[a].append([b,l])
    cost[b].append([a,l])


ans = 0
for i in range(1, n+1):
    s = 0
    dist = dijkstra(i)
    for j in range(1, n+1):
        if(dist[j] <= m):
            s += item[j-1]
    ans = max(s, ans)   
        
print(ans)

