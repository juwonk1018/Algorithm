import sys
input = sys.stdin.readline

n = int(input())

edge = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

selectVertex = set()
visited = [0] + [0] * n

queue = []

for i in range(1, n+1):
    if(len(edge[i]) == 1): # 연결된 edge가 하나라면
        queue.append(i)
        
while(queue):
    cur = queue.pop()
    if(visited[cur]):
        continue
    sVertex = edge[cur][0]
    selectVertex.add(sVertex)
    
    for v in edge[sVertex] + []:
        edge[sVertex].remove(v)
        edge[v].remove(sVertex)
        if(len(edge[v]) == 1 and visited[v] == 0):
            queue.append(v)
        
        if(len(edge[v]) == 0):
            visited[v] = 1
    
    visited[sVertex] = 1


print(len(selectVertex))
