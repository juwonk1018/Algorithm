import sys
input = sys.stdin.readline

n, play = input().split()
n = int(n)

name = set()
p = ["","Y","F","O"]
for _ in range(n):
    name.add(input().strip())


print(len(name) // (p.index(play)))
    