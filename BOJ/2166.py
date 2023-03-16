#오목 다각형을 생각해, ans += |ad -bc|에는 절대값을 붙히면 안된다.

import sys

input = sys.stdin.readline
n = int(input())

arr = []
moveX = moveY = 0
for i in range(n):
    x, y = map(int, input().split())
    if(i==0):
        moveX = x; moveY = y
    arr.append([x - moveX, y - moveY])
''
ans = 0
for i in range(0, len(arr)-1):
    ans += arr[i][0] * arr[i+1][1] - arr[i][1] * arr[i+1][0] # |ad - bc|

print(round(abs(ans)/2, 1))    