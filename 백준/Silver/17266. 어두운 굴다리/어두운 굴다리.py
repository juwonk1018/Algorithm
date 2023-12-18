import sys, math

input = sys.stdin.readline

n = int(input())
m = int(input())

positions = [0] + list(map(int, input().split())) + [n]

ans = 1
for i in range(1, m+1):
    
    # 왼쪽
    if(i == 1):
        ans = max(ans, positions[i])
    else:
        ans = max(ans, (math.ceil((positions[i] - positions[i-1])/2)))

    # 오른쪽
    if(i == m):
        ans = max(ans, n - positions[i])
    else:
        ans = max(ans, (math.ceil((positions[i+1] - positions[i])/2)))
    
print(ans)