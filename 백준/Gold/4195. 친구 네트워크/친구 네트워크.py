import sys

input = sys.stdin.readline

t = int(input())

def find(child):
    if(parent[child] != child):
        parent[child] = find(parent[child])
    return parent[child]

def union(c1, c2):
    p1 = find(c1)
    p2 = find(c2)

    if(p1 < p2):
        parent[p2] = p1
        parent_count[p1] += parent_count[p2]
        parent_count[p2] = 0
    elif(p1 > p2):
        parent[p1] = p2
        parent_count[p2] += parent_count[p1]
        parent_count[p1] = 0

    elif(p1 == p2):
        return
    


for _ in range(t):

    parent = dict()
    parent_count = dict()
    f = int(input())

    for _ in range(f):
        f1, f2 = input().split()
        if(f1 not in parent):
            parent[f1] = f1
            parent_count[f1] = 1
        if(f2 not in parent):
            parent[f2] = f2
            parent_count[f2] = 1

        union(f1, f2)
        if(parent[f1] == parent[f2]):
            print(parent_count[parent[f1]])
        else:
            print(parent_count[parent[f1]] + parent_count[parent[f2]])

