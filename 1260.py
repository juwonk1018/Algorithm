import sys
input = sys.stdin.readline

n,m,v = map(int,input().strip().split())
arr = [[] for i in range(n+1)]

for _ in range(m):
    a1, a2 = map(int,input().strip().split())
    arr[a1].append(a2)
    arr[a2].append(a1)

for k in range(n+1):
    arr[k].sort()

#dfs
dfs_visited = []
cur = [v]
while(cur):
    node = cur.pop(0)
    if(node not in dfs_visited):
        dfs_visited.append(node)
        cur = arr[node] + cur
        
        
print(' '.join(map(str,dfs_visited)))

#bfs
bfs_visited = []
cur = [v]
while(cur):
    node = cur.pop(0)
    if(node not in bfs_visited):
        bfs_visited.append(node)
        cur.extend(arr[node])               
            
print(' '.join(map(str,bfs_visited)))
