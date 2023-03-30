# 1) 부모 노드들로부터 거리를 모두 측정하여 부모가 없는 노드(루트노드) 부터의 거리를 서로 빼기
# 2) leaf node가 아닌 노드들의 자식들을 모두 구해 거리의 합을 구하기 => 1의 자식과 3의 자식이 겹칠수도 있어서 안됨..

# SOL) DFS를 통해 어떤 점에서 가장 먼 점을 구하고 그 점에서 가장 먼 점을 구하면 지름.... => 나중에 다시 보기
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

dist = [[] for _ in range(n+1)]

for i in range(n-1):
    p, c, weight = map(int, input().split())
    dist[p].append([c, weight])
    dist[c].append([p, weight])

# 1에서 가장 먼 노드를 찾기
distance = [-1] * (n+1)
distance[1] = 0
queue = deque([[1,0]])

while(queue):
    node, weight = queue.popleft()
    if(dist[node] != []):
        for node2, weight2 in dist[node]:
            if(distance[node2] == -1):
                distance[node2] = weight + weight2
                queue.append([node2, weight + weight2])


#가장 먼 노드에서 가장 먼 노드 = 트리의 지름
startNode = distance.index(max(distance))
distance = [-1] * (n+1)
distance[startNode] = 0
queue = deque([[startNode, 0]])

while(queue):
    node, weight = queue.popleft()
    if(dist[node] != []):
        for node2, weight2 in dist[node]:
            if(distance[node2] == -1):
                distance[node2] = weight + weight2
                queue.append([node2, weight + weight2])

print(max(distance))
