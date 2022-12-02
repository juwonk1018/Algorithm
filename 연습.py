n = int(input())
for i in sorted([*map(int,input().split())] for _ in range(n)):
    print(*i)
