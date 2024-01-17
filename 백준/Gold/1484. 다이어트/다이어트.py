import sys

input = sys.stdin.readline

g = int(input())

rw, cw = 1, 2

ans = []
while(True):
    if(cw**2 - (cw-1)**2 > g):
        break

    if(cw**2 - rw**2 < g):
        cw += 1
    elif(cw**2 - rw**2 == g):
        ans.append(cw)
        cw += 1
    elif(cw**2 - rw**2 > g):
        rw += 1

ans.sort()

if(ans):
    for i in ans:
        print(i)
else:
    print(-1)
