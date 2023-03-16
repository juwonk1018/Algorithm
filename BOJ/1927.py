import heapq
import sys

input = sys.stdin.readline

arr = []

n = int(input())

for _ in range(n):
    c = int(input())
    if(c):
        heapq.heappush(arr, c)
    else:
        if(arr):
            print(heapq.heappop(arr))
        else:
            print(0)