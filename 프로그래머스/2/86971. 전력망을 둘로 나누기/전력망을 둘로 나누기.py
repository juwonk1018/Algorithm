from collections import deque

def solution(n, wires):
    def search(idx):
        visited = [0] * (n+1)
        visited[idx] = 1 # 이 부분이 없으면 끊겨서 혼자만 남은 부분의 크기가 0이 된다.
        
        q = deque([idx])
        while(q):
            cur = q.popleft()
            for nextVertex in edge[cur]:
                if(visited[nextVertex] == 0):
                    visited[nextVertex] = 1
                    q.append(nextVertex)
                    
        return sum(visited)
    
    edge = [[] for _ in range(n+1)]
    answer = float("INF")
    
    for wire in wires:
        s, d = wire
        edge[s].append(d)
        edge[d].append(s)
        
    for wire in wires:
        start, dest = wire
        
        edge[start].pop(edge[start].index(dest))
        edge[dest].pop(edge[dest].index(start))
        m = search(start)
        edge[start].append(dest)
        edge[dest].append(start)
        
        answer = min(answer, abs(n-m-m))
        
    return answer