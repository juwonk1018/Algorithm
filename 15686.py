import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = []
house = []
chick = []
for _ in range(n):
    city.append(list(map(int, input().split())))

result = float("inf")

for i in range(n):
    for j in range(n):
        if(city[i][j] == 1):
            house.append([i,j])
        elif(city[i][j] == 2):
            chick.append([i,j])


for comb in combinations(chick, m):
    total = 0
    for h in house:
        val = float("inf")
        for c in comb:
            val = min(val, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        total += val
    result = min(total, result)


print(result)


#첫 시도는 BFS를 이용해 모든 house와의 거리, house와 chicken 가게의 의존성(가장 가까운 집이 몇 개 인지)를 고려했지만, 시간초과
#두번째 시도는 backtracking을 이용해, 함수를 정의해 n-queen 방식으로 늘려갔지만, 시간초과
#마지막으로 combinations를 이용해 시간초과 해결... 속도를 위해서 무조건 combinations를 써야되는 것인가?