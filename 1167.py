import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
node = [[] for _ in range(v+1)]
for i in range(1,v+1):
    inp = list(map(int, input().split()))
    for j in range(1, len(inp), 2):
        if(inp[j] == -1):
            break
        node[inp[0]].append([inp[j], inp[j+1]])
ans = 0

visited = [0] * (v+1)
queue = deque()
queue.append([1, 0])
visited[1] = 1

while(queue):
    cur, total = queue.popleft()
    
    for num, cost in node[cur]:
        if(visited[num] == 0):
            queue.append([num, total+cost])
            visited[cur] = 1
            if(ans < total+cost):
                ans = total+cost
                bfs_start = num
            

visited = [0] * (v+1)
queue = deque()
queue.append([bfs_start, 0])
visited[bfs_start] = 1
while(queue):
    cur, total = queue.popleft()
    for num, cost in node[cur]:
        if(visited[num] == 0):
            if(ans < total+cost):
                ans = total+cost
            queue.append([num, total+cost])
            visited[num] = 1
print(ans)

#첫번째 시도 : 각 vertex에서 BFS를 돌려 가장 긴 값을 ans로 둬서 출력. 예상대로 시간초과 O(V+E)에서 E가 n(n+1)/2까지 가능하므로
#두번째 시도 : edge가 하나인 node만이 최대 거리가 될 수 있으므로 이를 따로 list로 만듬, edge가 하나인 노드의 배열을 정렬해, for문을 돌려 해당 노드 앞까지는 모두 방문으로 처리
#세번째 시도 : (힌트, 질문 참고) 아무 점에서 BFS를 돌려 가장 긴 거리를 찾으면, 그 끝은 전체에서 가장 큰 거리의 끝점이다. 이후, BFS를 이 점을 시작점으로 해서 다시 돌리면 정답

# 주의
### - input이 숫자 순서대로가 아닌 것을 명심.
### - Cycle은 고려 X? 트리는 cycle이 없이 모든 정점이 연결되어 있는 그래프. 즉, 노드 N개에 간선이 N-1개.