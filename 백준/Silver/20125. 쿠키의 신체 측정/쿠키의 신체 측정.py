import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

ans = [0, 0, 0, 0, 0] # 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽다리, 오른쪽다리
def findCookieHead():
    for i in range(n):
        for j in range(n):
            if(arr[i][j] == '*'):
                return [i,j]

hx, hy = findCookieHead()        

ws = hx + 1

height = 1
while(ws + height < n and arr[ws + height][hy] == "*"):
    height += 1

we = hx + height

# 왼쪽 팔
for i in range(hy - 1,-1,-1):
    if(arr[ws][i] == "_"):
        ans[0] = hy-i-1
        break
else:
    ans[0] = hy

# 오른쪽 팔
for i in range(hy + 1 ,n):
    if(arr[ws][i] == "_"):
        ans[1] = i-hy-1
        break
else:
    ans[1] = n-1-hy

# 허리

ans[2] = we-ws

# 왼쪽 다리 : [we+1, hy-1] 시작

for i in range(we+1, n):
    if(arr[i][hy-1] == "_"):
        ans[3] = i-we-1
        break
else:
    ans[3] = n-1-we

# 오른쪽 다리
for i in range(we+1, n):
    if(arr[i][hy+1] == "_"):
        ans[4] = i-we-1
        break
else:
    ans[4] = n-1-we

print(hx+2, hy+1)
print(*ans)