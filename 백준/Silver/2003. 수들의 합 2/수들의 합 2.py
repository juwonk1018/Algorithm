import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

i, j = 0, 0

s = arr[0]

ans = 0
while(i < n and j < n):
    if(s < m):
        j += 1
        if(j < n):
            s += arr[j]

    elif(s > m):
        s -= arr[i]
        i += 1
        

    elif(s == m):
        ans += 1
        s -= arr[i]
        i += 1
        

print(ans)