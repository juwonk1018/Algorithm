# LIS (이분탐색 + 역추적) - 나중에 다시 살펴보기

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cp = [arr[0]]
dp = [0] * n

def binarySearch(item):
    left = 0; right = len(cp) - 1
    while(left < right):
        mid = (left + right)//2
        if(cp[mid] < item):
            left = mid + 1
        else:
            right = mid
    return left


for i in range(len(arr)):
    if(arr[i] > cp[-1]):
        cp.append(arr[i])
        dp[i] = len(cp)

    else:
        idx = binarySearch(arr[i])
        cp[idx] = arr[i]
        dp[i] = idx+1

ans = max(dp)
ansSeq = []

cur = ans
for i in range(n-1, -1, -1):
    if(dp[i] == cur):
        ansSeq.append(arr[i])
        cur -= 1

ansSeq.sort()

print(ans)
print(*ansSeq)
