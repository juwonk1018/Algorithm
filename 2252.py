import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [[] for i in range(n+1)]
child = [[] for i in range(n+1)]
#count = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    child[a].append(b)
    parent[b].append(a)
    #count[b] += 1

present = set()
remain = deque([i for i in range(1,n+1)])
result = []

while(remain):
    i = remain.popleft()        

    if(i in present): #memoization을 통해, 시간이 많이 줄어듦.
        continue

    exist = True
    for element in parent[i]:
        if(element not in present):
            exist = False
            break
    if(exist):
        result.append(i)
        present.add(i)
        for c in child[i]:
            remain.append(c)

print(*result)

# 부모가 둘 이상인 경우도 생각
# bottom-up : 어떤 element의 부모들을 모두 탐색해가면서 실시간으로 출력 후, visited를 memoization해 시간을 줄임. (recursion을 이용해야 편함)
# top-down : 해당 자식들을 탐색 후, count를 줄여 0이 되면 result에 포함되어 있으면 출력
# -> 바로 위의 부모가 자식에게 count를 줄여주고, 해당 자식들의 count만 확인해서 빠르게 result를 완성

# bottom up 방식

# if(count[i] == 0):
#     result.append(i)
#     for element in child[i]:
#         count[element] -= 1
#         if(count[element] == 0):
#              remain.append(element) 
# else:
#     remain.append(i)
