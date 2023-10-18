import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

def find(child):
    if(parent[child] != child):
        parent[child] = find(parent[child])
    return parent[child]

def union(c1, c2):
    p1 = find(c1)
    p2 = find(c2)

    if(p1 < p2):
        parent[p2] = p1
    elif(p2 > p1):
        parent[p1] = p2

parent = [i for i in range(n+1)]

for i in range(n):
    roads = list(map(int, input().split()))
    for j in range(n):
        if(roads[j]):
            union(i+1, j+1)

tripList = list(map(int, input().split()))

prevParent = find(tripList[0])

for i in range(1, m):
    if(find(tripList[i]) != prevParent):
        print("NO")
        break
    
    prevParent = find(tripList[i])
else:
    print("YES")