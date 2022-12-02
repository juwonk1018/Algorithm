import sys
input = sys.stdin.readline

num = int(input().strip())

arr = list(map(int, input().strip().split()))
ans = [[0,0] for _ in range(num+1)]
ans[0][0] = arr[0]
m = -100000

for i in range(1, num):
    ans[i][0] = max(ans[i-1][0] + arr[i], arr[i]) # 수를 제거하지 않은 경우
    ans[i][1] = max(ans[i-1][1] + arr[i], ans[i-1][0]) # 수를 제거한 경우
    m = max(m,ans[i][0],ans[i][1])

if(num == 1):
    m =arr[0]
    
print(m)
