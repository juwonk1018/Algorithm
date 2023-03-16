# gi를 시작으로 내림차순으로 빈 게이트가 있다면 비행기를 해당 게이트에 도킹
# 하지만, 내림차순을 linear하게 search시 시간초과.

# => 빈 공간을 빨리 찾는 방법 : 비행기가 해당 gate를 차지할 시, 자신이 바라보는 부모의 pointer를 parent - 1로 지정
# => find시 parent[child] = find(parent[child])로 찾자마자 갱신하면 시간이 많이 줄어든다.

# => Union-find 경로압축의 필요성

import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

g = int(input())
p = int(input())
gate = [0] * (g+1)

def find(child):
    if(parent[child] == child):
        return child
    parent[child] = find(parent[child])
    return parent[child]
    
parent = [i for i in range(g+1)] # gi가 들어왔을 때 도킹할 게이트의 위치

for _ in range(p):
    gi = int(input())
    if(gate[0] == 0):
        parent_plane = find(gi)
        gate[parent_plane] = 1
        parent[parent_plane] = find(parent_plane - 1)

print(sum(gate[1:]))