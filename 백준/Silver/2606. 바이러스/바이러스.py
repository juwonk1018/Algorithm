from collections import defaultdict, deque
n = int(input())
m = int(input())
pair = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    pair[a].append(b)
    pair[b].append(a)

path = set()
now = deque([1])
while(now):
    cur = now.popleft()
    for a in pair[cur]:
        if(a not in path and a != 1):
            now.append(a)
        if(a != 1):
            path.add(a)

print(len(path))