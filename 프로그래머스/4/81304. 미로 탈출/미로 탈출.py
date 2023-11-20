from heapq import heappush, heappop

def solution(n, start, end, roads, traps):
    
    answer = 1000000000
    
    edge = [[] for _ in range(n+1)]
    dist = {}
    
    trapIndex = {trap : n for n, trap in enumerate(traps)}
    
    for s, d, time in roads:
        edge[s].append([d,time])
        edge[d].append([s,-time])
    
    q = [[0, start, 0]] # [distance, vertex, bitmask]
    
    while(q):
        
        total, cur, mask = heappop(q)
        if(dist.get((cur, mask))): # 이미 존재한다면, 최선의 거리이므로 SKIP.
            continue
        
        if(cur == end):
            answer = total
            break
            
        dist[(cur, mask)] = total
        
        currentActivated = 1
        if(cur in traps and mask & (1 << trapIndex[cur])):
            currentActivated *= -1
            
        for nextVertex, time in edge[cur]:
            nextActivated = 1
            nextMask = mask
            if(nextVertex in traps):
                if(mask & 1<<trapIndex[nextVertex]):
                    nextActivated *= -1
                
                
                nextMask = nextMask ^ (1<<trapIndex[nextVertex])
            
            
            time *= currentActivated * nextActivated

            if(time > 0):
                heappush(q, [total + time, nextVertex, nextMask])
            
                    
    
    return answer