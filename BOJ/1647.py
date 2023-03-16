# 두 마을로 구분, 각 마을의 집은 어떻게든 갈 수만 있으면 됨 (= 사이클이 없는 최소 신장 트리)
# MST 문제. (Kruskal을 진행하면서 두 마을로 구분할 수 있는지 확인?)
# 마지막 추가된 간선이 두 마을을 잇는 간선이므로, 간선의 cost를 array에 모아서 마지막 cost를 제거하고 합을 구해도 나옴.
# -> partition과 break를 사용하지 않고도 문제를 풀 수 있음.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cost = []
for _ in range(m):
    a, b, c = map(int, input().split())
    cost.append([c, a, b])
cost.sort() # 오름차순으로 정렬


parent = [i for i in range(n+1)]

def find(child):
    if(child != parent[child]):
        parent[child] = find(parent[child]) # parent[child]의 부모를 find로 찾아서 parent[child] 지정시키기
    return parent[child]

def union(a,b):
    parent_a = find(a) 
    parent_b = find(b)
    if(parent_a < parent_b):
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

partition = n
ans = 0; cur = 1


for i in range(len(cost)):
    c, a, b = cost[i]
    if(find(a) != find(b)):
        union(a,b)
        ans += c
        partition -= 1

    if(partition == 2):
        break
print(ans)