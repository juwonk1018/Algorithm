import heapq
def solution(n, edge):
    edges = [[] for _ in range(n+1)]
    for s, e in edge:
        edges[s].append(e)
        edges[e].append(s)
        
    visited = [-1] * (n+1)
    
    visited[1] = 0
    hq = [[0, 1]]
    while(hq):
        dist, vertex = heapq.heappop(hq)
            
        for v in edges[vertex]:
            if(visited[v] == -1):
                visited[v] = dist + 1
                heapq.heappush(hq, [dist+1, v])
        
    return visited.count(max(visited))
    