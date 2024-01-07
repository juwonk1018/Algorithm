import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def find(c):
    if(c != parent[c]):
        parent[c] = find(parent[c])
    return parent[c]

def union(c1, c2):
    p1 = find(c1)
    p2 = find(c2)

    if(p1 < p2):
        parent[p2] = p1
    else:
        parent[p1] = p2

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    command, a, b = map(int, input().split())

    if(command == 0):
        union(a,b)
    elif(command == 1):
        if(find(a) == find(b)):
            print("YES")
        else:
            print("NO")