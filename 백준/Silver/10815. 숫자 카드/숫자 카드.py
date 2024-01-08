import sys
input = sys.stdin.readline

n = int(input())

card = set()
ans = []

for i in list(map(int, input().split())):
    card.add(i)

m = int(input())


for i in list(map(int, input().split())):
    ans.append(1 if i in card else 0)

print(*ans)

