import sys
input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

parent = [-1 for _ in range(n+1)]

queue = [[1, arr[1]]]
while(queue):
    idx, nodes = queue.pop()
    for node in nodes:
        if(parent[node] == -1):
            parent[node] = idx
            queue.append([node, arr[node]])

print(*parent[2:], sep = "\n")