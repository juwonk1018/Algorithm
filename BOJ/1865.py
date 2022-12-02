from collections import deque
import sys
input = sys.stdin.readline
INF = int(2e9)
tc = int(input())


for _ in range(tc):
    
    n, m, w = map(int, input().split())
    cost = [[] for _ in range(n+1)] 

    for _ in range(m): #도로의 정보
        s, e, t = map(int, input().split())
        cost[s].append([e,t])
        cost[e].append([s,t])
    for _ in range(w): #웜홀의 정보
        
        s, e, t = map(int, input().split())
        if(t!=0):
            cost[s].append([e,-t])

    

    found = False

    dist = [INF] * (n+1)
    dist[1] = 0
    for i in range(n):
        for j in range(1,n+1):
            for dst, time in cost[j]:
                if(dist[j] + time < dist[dst]):
                    if(i==n-1):
                        found = True
                    dist[dst] = dist[j] + time
    
    if(found):
        print("YES")
    elif(not(found)):
        print("NO")


# BFS로 풀이시 35%에서 틀림으로 표기됨.

# 벨만포드 : V-1 cycle까지 distance를 update 후, V번째 cycle에서 update가 되면 음수 cycle이 존재함.

# if(dist[j] != INF) 조건이 붙으면 틀리는데, 이는 시작점으로부터 dist[j]까지 갈 수 있는지를 의미함.
# 위의 조건이 삭제되면, INF 상태의 dist[v]는 INF인 거리를 통해 v에 방문할 수 있다는 것으로 인식해 v에 연결된 edge도 고려하게 된다.
# -> 즉, 모든 vertices에 대해 벨만포드 알고리즘을 적용시키지 않아도 된다.

# float("inf")는 float("inf") - 1도 float("inf")로 저장되므로 update가 된 것 처럼 보이지 않음 -> int(2e9)로 변경