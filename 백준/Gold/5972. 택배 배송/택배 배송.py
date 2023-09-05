import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())

costs = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a].append([b,c])
    costs[b].append([a,c])


def dijkstra():
    visited = [0] * 2 + [float("INF")] * (n-1)
    
    hq = [[0, 1]]

    while(hq):
        cow, cur = heapq.heappop(hq)
        
        if(visited[cur] < cow):
            continue

        for dest, cost in costs[cur]:
            total = cow + cost
            if(visited[dest] > total):
                visited[dest] = total
                heapq.heappush(hq, [total, dest])

    print(visited[n])

dijkstra()