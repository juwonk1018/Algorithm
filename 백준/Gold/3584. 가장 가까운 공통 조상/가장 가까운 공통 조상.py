import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    parent = [i for i in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a

    n1, n2 = map(int, input().split())

    parents_n1 = [n1]
    parents_n2 = []

    while(parent[n1] != n1):
        parents_n1.append(parent[n1])
        n1 = parent[n1]

    while(True):
        if(parent[n2] in parents_n1):
            print(parent[n2])
            break

        n2 = parent[n2]


