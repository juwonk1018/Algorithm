import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
totalSum = [0 for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    totalSum[child] = totalSum[parent] + weight
    
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])
    

maxSum = max(totalSum)
maxIdx = -1

for i in range(1,n+1):
    if(totalSum[i] == maxSum):
        maxIdx = i
        break

result = 0

queue = deque()
queue.append([i,0])
visited = [0 for i in range(n+1)]
visited[i] = 1
while(queue):
    node, value = queue.popleft()
    for neighbor in tree[node]:
        if(visited[neighbor[0]] == 0):
            queue.append([neighbor[0], neighbor[1] + value])
            visited[neighbor[0]] = 1
            if(neighbor[1] + value > result):
                result = neighbor[1] + value

print(result)

#1차 시도 : root에서부터 가장 큰 가중치를 가진 leaf node를 찾아서, 다른 leaf node와의 공통 parent를 찾아 공통 부분을 제거해서 답을 구함 -> 메모리초과
#2차 시도 : root에서부터 가장 큰 가중치를 가진 leaf node를 찾아, BFS