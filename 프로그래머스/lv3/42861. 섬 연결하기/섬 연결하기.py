import heapq

def solution(n, costs):
    
    def find(child):
        if(child == parent[child]):
            return child
        
        parent[child] = find(parent[child])
        return parent[child]
    
    def union(c1, c2):
        p1, p2 = find(c1), find(c2)
        if(p1 < p2):
            parent[p2] = p1
        else:
            parent[p1] = p2
    
    hq = []
    parent = [i for i in range(n)]
    answer = 0
    cnt = 1
    
    for s, e, c in costs:
        heapq.heappush(hq, [c, s, e])
    
    while(cnt != n):
        c, s, e = heapq.heappop(hq)
        if(find(s) != find(e)):
            answer += c
            cnt += 1
            union(s, e)
            
    
    return answer