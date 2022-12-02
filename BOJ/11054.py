import sys
input = sys.stdin.readline


line = int(input().strip())

num = list(map(int,input().strip().split()))
arr1 = [0]*1001
arr2 = [0]*1001

ans = 0
ans1 = []
ans2 = []

for s in num:
    arr1[s] = max(arr1[:s]) + 1
    ans1.append(max(arr1))

for s in list(reversed(num)):
    arr2[s] = max(arr2[:s]) + 1
    ans2.append(max(arr2))

for i in range(0,line):
    ans = max(ans, ans1[i] + ans2[-i-1] - 1)

print(ans)
