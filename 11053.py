import sys
input = sys.stdin.readline

num = int(input())
arr = list(map(int, input().strip().split()))

ans = [1]
for i in range(1,num):    
    temp = [1]
    for j in range(0,i):
        if(arr[j] < arr[i]):
            temp.append(ans[j] + 1)
    ans.append(max(temp))

print(max(ans))


# 1000개의 범위밖에 안되므로, dp = [0] * 1001을 하여,
# for s in arr: ans[s] = max(ans[:s]) + 1로 표기해도 무방


