import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if(i>0):
            arr[i][j] += arr[i-1][j]
        if(j>0):
            arr[i][j] += arr[i][j-1]
        if(i>0 and j>0):
            arr[i][j] -= arr[i-1][j-1]

result = []
for _ in range(m):
    x1,y1, x2,y2 = map(int, input().split())
    sum = arr[x2-1][y2-1]
    if(x1 >= 2):
        sum -= arr[x1-2][y2-1]
    if(y1 >= 2):
        sum -= arr[x2-1][y1-2]
    if(x1 >=2 and y1 >=2):
        sum += arr[x1-2][y1-2]
    result.append(sum)

print(*result, sep = "\n")

#내가 한 풀이가 DP였넹..