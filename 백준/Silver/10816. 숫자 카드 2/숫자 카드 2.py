import sys

input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
dic = dict()
for i in range(n):
    if(arr[i] not in dic):
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

m = int(input())
arr2 = list(map(int, input().split()))

ans = []
for i in range(m):
    if(arr2[i] in dic):
        ans.append(dic[arr2[i]])
    else:
        ans.append(0)

print(*ans)
