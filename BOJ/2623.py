import sys
input = sys.stdin.readline

m, n = map(int, input().split())

req_list = [[] for _ in range(m+1)]
req = [0 for _ in range(m+1)]

for _ in range(n):
    cur = list(map(int, input().split()))
    for i in range(1, cur[0]+1):
        if(i != cur[0]):
            req_list[cur[i]] += cur[i+1:]
        req[cur[i]] += i-1

ans = []
for _ in range(m):
    next = -1
    for i in range(1, m+1):
        if(req[i] == 0):
            next = i
            for item in req_list[next]:
                req[item] -= 1
            break
    
    if(next != -1):
        req[next] = -1
        ans.append(next)
    else:
        ans = []
        break
    
if(ans == []):
    print(0)
else:
    print(*ans, sep = "\n")
            