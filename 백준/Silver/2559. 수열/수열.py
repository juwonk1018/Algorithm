import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, k-1

s = sum(arr[start:end+1])

ans = -float("INF")
while(end < n):
    ans = max(ans, s)

    s -= arr[start]
    start, end = start + 1, end + 1
    if(end < n):
        s += arr[end]

    
print(ans)