# 2개의 경우 : a-b, b-a
# 4개의 경우 : a-b+c-d, a-b+d-c, b-a+c-d, b-a+d-c  ab/cd
#            : a-c+b-d, a-c+d-b, c-a+b-d, c-a+d-b  ac/bd
#            : a-d+b-c, a-d+c-b, d-a+b-c, d-a+c-b  ad/bc

# 즉, n개에서 n/2개만큼 -를 고르기. (전체 좌표를 다 더하고 n/2개에 해당되는 값을 두 번 빼기)

import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    pos = []
    for _ in range(n):
        pos.append(list(map(int, input().split())))

    tx, ty = 0, 0
    for i in range(n):
        tx += pos[i][0]
        ty += pos[i][1]


    ans = float("INF")

    for arr in combinations(pos, n//2):
        cx, cy = tx, ty # 값을 복사
        for x,y in arr:
            cx -= 2*x
            cy -= 2*y

        ans = min(ans, (cx**2+cy**2)**(1/2))

    print(ans)