# 시간 제한이 0.6초라서 정렬 후 가운데 고르기는 시간초과 가능성

# 정렬 후 가운데 index 고르기?

# 왼쪽, 오른쪽에 heapq를 사용해 왼쪽은 최대 힙을 이용해 중간값에 가장 가까운 최대값을, 오른쪽은 최소값으로 중간값 계속 결정
# cur을 이용하지 않고 heapq만 2개 사용하여도 풀 수 있음

import sys
import heapq

input = sys.stdin.readline

maxh = []; minh = []
n = int(input())

cur = int(input())
print(cur)
for i in range(n-1):
    a = int(input())
    if(a < cur):
        heapq.heappush(maxh, -a)
    else:
        heapq.heappush(minh, a)
    
    if(len(maxh) > len(minh)): # 평균보다 작은 수의 개수가 많다면
        heapq.heappush(minh, cur)
        cur = -heapq.heappop(maxh)

    if(len(maxh) + 2 == len(minh)): # 평균보다 큰 수가 많다면 더 작은 수는 maxheap에, 큰 수는 cur로
        heapq.heappush(maxh, -cur)
        cur = heapq.heappop(minh)
    print(cur)