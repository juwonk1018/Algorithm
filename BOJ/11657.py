import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b,c])


def bf():
    distance = [float("INF")] * (n+1)
    distance[1] = 0
    for _ in range(n):
        for i in range(1, n+1):
            for dest, cost in edges[i]:
                distance[dest] = min(distance[dest], distance[i] + cost)

    for i in range(1, n+1): # Cycle 확인
        for dest, cost in edges[i]:
            if(distance[dest] > distance[i] + cost):
                return [-1]

    return distance

answer = bf()

if(answer != [-1]):
    answer = answer[2:]
    answer = [-1 if i == float("INF") else i for i in answer]

print(*answer, sep ="\n")