def solution(edges):
    def search(edge, idx):
        visited = set()
        q = [idx]
        while(q):
            cur = q.pop()
            visited.add(cur)
            if(len(edge[cur]) >= 2):
                return 2
            
            elif(len(edge[cur]) == 0):
                return 1
            
            nextVertex = edge[cur][0]
            if(nextVertex in visited): # 이미 방문했다면, 도넛 모양
                return 0
            
            q.append(nextVertex)
        return 0
        
    n = max(map(max, edges))
    inDegree = [0] * (n+1)
    edge = [[] for _ in range(n+1)]
    
    for start, end in edges:
        edge[start].append(end)
        inDegree[end] += 1
    
    for i in range(1, n+1):
        if(len(edge[i]) >= 2 and inDegree[i] == 0):
            newVertex = i
            break
    
    graphNumber = [0,0,0]
    for vertex in edge[newVertex]:
        graphNumber[search(edge, vertex)] += 1
        
    answer = [newVertex] + graphNumber
    return answer