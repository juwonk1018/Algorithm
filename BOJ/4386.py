# 각 점에서 갈 수 있는 최소 거리를 n-1개 구하는 방식 -> cycle이 만들어지면 오답
# Union-find를 이용해 최소 거리 n-1 search -> 4 / 1 1 / 3 3 / 2 2 / 4 4의 예시에 적용이 안됨
# Prim, Kruskal 둘 다 사용해도 O

# Prim을 이용한 풀이) heapq를 이용해서 새로운 점마다 edge를 heap에 넣고 지나온 point인지만 check하는 방법도 존재
# => 지나온 점에서 모든 edge를 for문에서 매번 갱신안해도 됨.
import sys
input = sys.stdin.readline

n = int(input())

pos = []
for i in range(n):
    x, y = map(float, input().split())
    pos.append([x,y])




dist = [[float("INF")] * (n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(i != j):
            distance = ((pos[j][0] - pos[i][0]) ** 2 + (pos[j][1] - pos[i][1]) **2) ** (1/2)
            dist[i][j] = dist[j][i] = distance 


ans = 0
points = [0]
check = [1] * n; check[0] = 0
while(len(points) != n):
    minD = float("INF")
    nextP = -1

    for point in points:
        for i in range(n): #현재 연결된 점들에서 나아갈 수 있는 최소 길이의 선분 탐색
            if check[i] and minD > dist[point][i]:
                    minD = dist[point][i] 
                    nextP = i
    ans += minD
    points.append(nextP)
    check[nextP] = 0

print(round(ans, 2))
