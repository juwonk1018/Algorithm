import sys

input = sys.stdin.readline

n, m = map(int, input().split())

notListend = set()
answer = []

for _ in range(n):
    name = input().strip()
    notListend.add(name)

for _ in range(m):
    name = input().strip()
    if(name in notListend):
        answer.append(name)

answer.sort()
print(len(answer))
for name in answer:
    print(name)