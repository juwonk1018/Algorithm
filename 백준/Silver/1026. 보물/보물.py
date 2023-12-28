import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr.sort()
arr2.sort(reverse = True)

ans = 0
for a, b in zip(arr, arr2):
    ans += a*b

print(ans)