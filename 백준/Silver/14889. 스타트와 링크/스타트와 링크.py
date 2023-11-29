import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

answer = float("INF")

score = [list(map(int, input().split())) for _ in range(n)]
arr = [i for i in range(n)]

for comb in combinations(arr, n//2):
    startScore = 0
    linkScore = 0
    
    startTeam = list(comb)
    linkTeam = list(set(arr) - set(comb))
    for i in startTeam:
        for j in startTeam:
            startScore += score[i][j]

    for i in linkTeam:
        for j in linkTeam:
            linkScore += score[i][j]
            
    answer = min(answer, abs(startScore-linkScore))

print(answer)