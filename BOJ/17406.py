from itertools import permutations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))



def rotate(arr, r, c, stride):
    new_arr = [arr[i][:] for i in range(n)]

    for i in range(1, stride+1): # 위쪽
        for j in range(c-i,c+i):
            new_arr[r-i][j+1] = arr[r-i][j]
    
    for i in range(1, stride+1): # 오른쪽
        for j in range(r-i,r+i):
            new_arr[j+1][c+i] = arr[j][c+i]

    for i in range(1, stride+1): # 아래쪽
        for j in range(c+i,c-i,-1):
            new_arr[r+i][j-1] = arr[r+i][j]

    for i in range(1, stride+1): # 왼쪽
        for j in range(r+i,r-i,-1):
            new_arr[j-1][c-i] = arr[j][c-i]

    return new_arr

rotateList = []

for i in range(k):
    r, c, s = map(int, input().split())
    rotateList.append([r-1,c-1,s])

ans = float("INF")
for rotateOrder in permutations(rotateList, k):
    result = [arr[i][:] for i in range(len(arr))]
    for rotateCommand in rotateOrder:
        r, c, s = rotateCommand
        result = rotate(result, r, c ,s)

    ans = min(ans, min(list(map(sum, result))))

print(ans)