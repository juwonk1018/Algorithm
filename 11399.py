import sys
input = sys.stdin.readline
n = int(input().strip())
arr = list(map(int, input().strip().split()))
arr.sort()
ans = [arr[i]*(len(arr)-i) for i in range(0,len(arr))]
print(sum(ans))
