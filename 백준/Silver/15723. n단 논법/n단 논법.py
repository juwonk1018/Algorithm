import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(27)]

for _ in range(n):
    c1, c2 = input().split("is")
    c1 = ord(c1.strip()) - 96
    c2 = ord(c2.strip()) - 96
    parent[c1] = c2


m = int(input())

for _ in range(m):
    c1, c2 = input().split("is")
    c1 = ord(c1.strip()) - 96
    c2 = ord(c2.strip()) - 96
    

    while(c1 != parent[c1]):
        if(parent[c1] == c2):
            break

        c1 = parent[c1]
    
    if(parent[c1] != c2):
        print("F")
    else:
        print("T")