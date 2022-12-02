import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            temp = arr[i]+arr[j]+arr[k]
            if(ans < temp and temp <= m):
                ans = temp

print(ans)
