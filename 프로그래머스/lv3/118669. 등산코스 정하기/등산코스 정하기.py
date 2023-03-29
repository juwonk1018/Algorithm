# Gate n -> Submit m -> Gate n 순

import heapq

def solution(n, paths, gates, summits):
    summits = set(summits)
    gates = set(gates)
    
    answer = []
    dist = [[] for _ in range(n+1)]
    
    for path in paths:
        i, j, w = path
        dist[i].append([j,w])
        dist[j].append([i,w])
    
    minDist = float("INF")
    minNum = 0
    for gate in gates:
        
        visited = [0] * (n+1)
        q = [[0, gate]]
        
        while(q):
            distance, target = heapq.heappop(q)

            if((distance > minDist) or visited[target]):
                continue
                
            if(gate != target and target in gates):
                continue
                
            if(target in summits):
                if(minDist > distance):
                    minDist = distance
                    minNum = target
                elif(minDist == distance):
                    minNum = min(target, minNum)
                    
                break

            visited[target] = 1
            for dst, target_distance in dist[target]:
                if(visited[dst] == 0 and max(distance, target_distance) <= minDist):
                    heapq.heappush(q, [max(distance, target_distance), dst])

    return [minNum, minDist]