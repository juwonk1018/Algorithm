# 고이는 빗물 = 왼, 오른쪽에 자신보다 높은 블록이 있어야된다.
import sys
input = sys.stdin.readline

h, w = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0

for i in range(1, w-1):
    ans += max(0, min(max(arr[:i]), max(arr[i+1:])) - arr[i])
print(ans)