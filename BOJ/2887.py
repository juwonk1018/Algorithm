# 3차원에서의 Kruskal Algorithm => distance가 100000C2개여서 초과될 수 있음
# x, y, z에서 n번째로 작은 차이를 가진 edge부터는 활용되지 않음.
# => x,y,z 좌표를 오름차순으로 정렬 후 인근 point들의 edge만 고려하여 답을 구함. (혼자 풀지 못했음)

# 파이썬은 1초에 2000만번의 연산, 128MB 기준으로 3000만개의 원소까지 가능

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

parent = [i for i in range(n)]

def find(c1):
    if(parent[c1] != c1):
        return find(parent[c1])
    return parent[c1]

def union(p1, p2):
    x1 = find(p1)
    x2 = find(p2)
    if(x1 < x2):
        parent[x2] = x1
    else:
        parent[x1] = x2

xlst = []; ylst = []; zlst = []

for i in range(n):
    x, y, z = map(int, input().split())
    xlst.append([x, i])
    ylst.append([y, i])
    zlst.append([z, i])

xlst.sort(); ylst.sort(); zlst.sort();

edges = []
for curList in xlst, ylst, zlst:
    for i in range(n-1):
        edges.append([curList[i+1][0] - curList[i][0], curList[i+1][1], curList[i][1]])

edges.sort()
edges = deque(edges)

num = 0; ans = 0
while(num != n-1):
    dist, a, b = edges.popleft()
    if(find(a) == find(b)):
        continue
    union(a,b)
    num += 1
    ans += dist

print(ans)
