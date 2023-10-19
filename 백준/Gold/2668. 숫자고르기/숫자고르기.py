import sys
input = sys.stdin.readline

parent = [0]

n = int(input())

for _ in range(n):
    parent.append(int(input()))

ans = []

for i in range(1, n+1):
    cur = i
    for _ in range(n):
        if(parent[cur] != i):
            if(parent[cur] == cur):
                break
            cur = parent[cur]
            
        else:
            ans.append(cur)
            break

ans.sort()
print(len(ans))
for i in ans:
    print(i)    