import sys
input = sys.stdin.readline


line = int(input().strip())

arr = [0] * 1001

for s in list(map(int,input().strip().split())):
    arr[s] = max(arr[s+1:] + [0]) + 1

print(max(arr))
