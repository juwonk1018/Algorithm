import sys
input = sys.stdin.readline
n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
arr.sort()
for i in range(n): print(*arr[i])
