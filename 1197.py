
"""
#Kruskal Algorithm

import sys
input = sys.stdin.readline

v,e = map(int, input().split())

edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append([c,a,b])

edge.sort()




parent = [i for i in range(v+1)]

def union(num1, num2):
    num1 = find(num1)
    num2 = find(num2)
    if(num1 > num2):
        parent[num1] = num2
    else:
        parent[num2] = num1

def find(num):
    if(parent[num] != num):
        parent[num] = find(parent[num])
    return parent[num]

sum = 0
for weight, v1, v2 in edge:
    p1 = find(v1)
    p2 = find(v2)
    if(p1 == p2):
        continue
    sum += weight
    union(v1, v2)
    
print(sum)
"""
#Prim Algorithm

import sys, heapq
input = sys.stdin.readline

v,e = map(int, input().split())

edge = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])


visited = [0 for _ in range(v+1)]

mst = [[0,1]]
sum = 0
cnt = 0
while(mst):
    if(cnt == v):
        break
    weight, dst = heapq.heappop(mst)
    if(visited[dst] == 0):
        for e in edge[dst]:
            heapq.heappush(mst, e)
        sum += weight
        visited[dst] = 1
        cnt += 1

print(sum)

#MST 해결방법은 Krusal Algorithm(Union-Find 이용), Prim Algorithm 존재
#Krusal Algorithm은 Union-Find 이용, Prim Algorithm은 min-heap 이용
#Prim에서 edge[1]로 시작하면, 해당 배열은 heap 구조를 이루지 않기 때문에 오답
#push하는 것이 list라면, heappush는 index 0을 기준으로 heap을 이룸