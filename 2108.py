import sys
from collections import Counter

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(round(sum(arr)/n))
print(arr[int(n/2)])
cnt = Counter(arr).most_common()

if(len(cnt) == 1):
    print(cnt[0][0])
else:
    if(cnt[0][1] == cnt[1][1]):
        print(cnt[1][0])
    else:
        print(cnt[0][0])
print(arr[n-1]-arr[0])

''' sys.stdin.readline()이 input()보다 속도가 빠름...
'''