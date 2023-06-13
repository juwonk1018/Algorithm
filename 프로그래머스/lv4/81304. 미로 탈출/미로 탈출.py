from heapq import heappush, heappop

def solution(n, start, end, roads, traps):
    
    def dijkstra(roadCost, s, e, totalTime, trapCount):
        nonlocal answer
        
        
        if(s==e):
            answer = 0
            return
        
        distance = [float("INF")] * (n+1)
        
        q = [[s, totalTime]]
        
        while(q):
            cur, curTime = heappop(q)
            
            if(distance[cur] < curTime or (cur != s and cur in traps)):
                continue
                
            for dest, time in roadCost[cur]:
                if(distance[dest] > curTime + time):
                    distance[dest] = curTime + time
                    heappush(q, [dest, curTime + time])

        
            
        if(distance[e] != float("INF")):
            answer = min(answer, distance[e])
        
        for idx, trap in enumerate(traps):
            if(distance[trap] < answer and trapCount[idx] < 2): # Trap을 밟음
                trapCountCopy = trapCount + []
                trapCountCopy[idx] += 1

                trapRoadCost = [[] for _ in range(n+1)]
                for i in range(len(roadCost)):
                    for j in range(len(roadCost[i])):
                        dest, time = roadCost[i][j]
                        if(i == trap or dest == trap):
                            trapRoadCost[dest].append([i, time])
                        else:
                            trapRoadCost[i].append([dest, time])

                dijkstra(trapRoadCost, trap, e, distance[trap], trapCountCopy)

    answer = 1000000000
    roadCost = [[] for _ in range(n+1)]
    
    for s, d, time in roads:
        roadCost[s].append([d,time])
        
    dijkstra(roadCost, start, end, 0, [0] * len(traps))
    
    return answer