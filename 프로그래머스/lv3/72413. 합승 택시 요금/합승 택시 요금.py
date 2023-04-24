
def solution(n, s, a, b, fares):
    dist = [[float("INF")] * (n+1) for _ in range(n+1)]
    for start, end, fare in fares:
        dist[start][end] = fare
        dist[end][start] = fare
    
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    
    answer = dist[s][a] + dist[s][b]
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
        
    return answer