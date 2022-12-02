import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(2e9)
arr = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    src, dst, cost = map(int, input().split())
    if(arr[src][dst] > cost):
        arr[src][dst] = cost

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if(j==k):
                arr[j][k] = 0
            else:
                arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if(arr[i][j] == INF):
            print("0", end = " ")
        else:
            print(arr[i][j], end = " ")

    print()
