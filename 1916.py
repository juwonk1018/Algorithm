import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())




bus = [[] for _ in range(n+1)]
for _ in range(m):
    src, dst, cost = map(int, input().split())
    bus[src].append([dst,cost])

start, end = map(int, input().split())
total = [float("INF")] * (n+1)
total[start] = 0

stack = deque()
stack.append(start)

while(stack):
    cur = stack.popleft()
    for dst, cost in bus[cur]:
        if(total[dst] > total[cur] + cost):
            total[dst] = total[cur] + cost
            if(dst not in stack):
                stack.append(dst)

print(total[end] - total[start])
