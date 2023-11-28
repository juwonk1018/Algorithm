import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(h+x)]
for i in range(x, h+x):
    for j in range(y, w+y):
        arr[i][j] -= arr[i-x][j-y]


for i in range(h):
    print(*arr[i][:w])
