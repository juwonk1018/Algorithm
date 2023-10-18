from itertools import combinations

n, m, k = map(int, input().split())

total = 0
ans = 0
for comb in combinations([i for i in range(1, n+1)], m):
    cnt = 0
    for i in range(1, m+1):
        if(i in comb):
            cnt += 1
    
    if(cnt >= k):
        ans += 1
    total += 1

print(ans/total)