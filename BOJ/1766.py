# 위상정렬 문제
# 
# 먼저 풀린 문제가, 뒤에 따라오는 문제들을 체크한 뒤에 heap에 넣고 heappop으로 최소값 구하기

import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

remain = [0] * (n+1)
precedence = [[] for _ in range(n+1)]
heap = []

for _ in range(m):
    n1, n2 = map(int, input().split())
    precedence[n1].append(n2)
    remain[n2] += 1

for i in range(1, n+1):
    if(remain[i] == 0):
        heapq.heappush(heap, i)
        remain[i] = -1

ans = []

for _ in range(n):
    cur = heapq.heappop(heap)
    ans.append(cur)
    for nextLevel in precedence[cur]:
        remain[nextLevel] -= 1
        if(remain[nextLevel] == 0):
            heapq.heappush(heap, nextLevel)
            remain[nextLevel] = -1 # 이 줄은 없어도 된다. (한번 0인게 체크가 되었으므로)

print(*ans)