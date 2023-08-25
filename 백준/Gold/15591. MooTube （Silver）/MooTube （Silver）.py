"""
존은 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO 중 최솟값으로 하기로 했다.
"""
import sys,copy
input=sys.stdin.readline
from collections import deque

def Find(x): # 유니온 파인드의 Find 함수
    if x!=disjoint[x]:
        disjoint[x] = Find(disjoint[x])
    return disjoint[x]

def Union(a,b): # 유니온 파인드의 Union 함수
    a=Find(a) ; b=Find(b)

    if a==b:
        return
    if a>b:
        disjoint[a]=b
        dp[b]+=dp[a]
    else:
        disjoint[b]=a
        dp[a]+=dp[b]

N,Q=map(int,input().split())

graph=[] # 트리를 저장할 그래프를 선언한다.
dp=[1]*(N+1)

for i in range(N-1):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))

graph.sort(key=lambda x:-x[2])
graph=deque(graph)
L=[ list(map(int,input().split())) for _ in range(Q) ] # 쿼리를 입력받는다.
Query=copy.deepcopy(L) # 쿼리를 미리 복사한다.

L.sort(key=lambda x:-x[0]) # k 값이 높은 순서대로 정렬한다.
disjoint=[ i for i in range(N+1) ] # 분리집합을 위한 배열을 만든다.

D={} # 오프라인 쿼리를 위한 딕셔너리
for K,V in L: # 쿼리 실행.
    while graph and graph[0][2]>=K:
        if Find(graph[0][0])!=Find(graph[0][1]):
            Union(graph[0][0] , graph[0][1])
            graph.popleft()
    D[(K,V)] = dp[Find(V)]-1

for K,V in Query: # 이전의 복사해둔 쿼리를 사용한다.
    print(D[(K,V)]) # 그때의 딕셔너리 값을 출력한다.