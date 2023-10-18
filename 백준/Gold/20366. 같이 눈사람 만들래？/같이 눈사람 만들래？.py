from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
snowball = list(map(int, input().split()))
snowball.sort()

p1 = 0; p2 = 3
p3 = 1; p4 = 2

ans = float("INF")

for i in range(n):
    for j in range(i+3, n):
        height = snowball[i] + snowball[j]
        left = i+1; right = j-1
        
        while(left < right):
            tempHeight = snowball[left] + snowball[right]
            if(tempHeight > height):
                right -= 1
            else:
                left += 1

            ans = min(ans, abs(height - tempHeight))

print(ans)