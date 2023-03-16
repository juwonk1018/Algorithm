# 각 point마다 BFS/DFS를 돌리기는 너무 무거움
# => Union-Find를 이용하여 parent가 같으면 cycle이 형성하는 것을 알 수 있음

import sys
input = sys.stdin.readline

n, m = map(int, input().split())


parent = [i for i in range(n)]

def find(child):
    if(parent[child] == child):
        return parent[child]
    return find(parent[child])
        

def union(c1, c2):
    p1 = find(c1)
    p2 = find(c2)
    if(p1 < p2):
        parent[p2] = p1
    else:
        parent[p1] = p2

ans = 0
for i in range(m):
    a, b = map(int, input().split())

    if(ans == 0):
        parentA = find(a)
        parentB = find(b)
        if(parentA != parentB):
            union(a, b)
        else:
            ans = i+1


print(ans)