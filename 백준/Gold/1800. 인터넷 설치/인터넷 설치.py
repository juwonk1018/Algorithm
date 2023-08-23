import sys, heapq
input = sys.stdin.readline

n, p, k = map(int, input().split())

edges = [[] for _ in range(n+1)]

for _ in range(p): # 유료 케이블선
    a, b, cost = map(int, input().split())
    edges[a].append([b, cost])
    edges[b].append([a, cost])

left, right = 0, 1000001

ans = float("INF")

def checkDijkstra(num):

    hq = [[0, 1]]
    visited = [float("INF")] * (n+1)
    visited[1] = 0

    while(hq):
        count, currentVertex = heapq.heappop(hq)
        
        if(currentVertex == n and count <= k):
            return True

        if(visited[currentVertex] < count):
            continue

        for nextVertex, nextCost in edges[currentVertex]:
            if(nextCost > num and count < k and visited[nextVertex] > count + 1):
                heapq.heappush(hq, [count + 1, nextVertex])
                visited[nextVertex] = count + 1
            elif(nextCost <= num and visited[nextVertex] > count):
                heapq.heappush(hq, [count, nextVertex])
                visited[nextVertex] = count
    
    return False

while(left < right):
    mid = (left + right)//2
    if(checkDijkstra(mid)):
        ans = min(ans, mid)
        right = mid
    else:
        left = mid + 1

print(ans if ans != float("INF") else -1)