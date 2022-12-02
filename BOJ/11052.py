import sys
input = sys.stdin.readline
num = int(input().strip())
arr = list(map(int,input().strip().split()))
arr.insert(0,0)

ans = [0]*(num+1) # i개를 고를 경우의 최대값 
ans[1] = arr[1]
for i in range(1,num+1):
    for j in range(1,i):
        ans[i] = max(ans[i], ans[j] + ans[i-j], arr[i])   
print(ans[num])
# for j in 부터 arr[i])까지 지우고
# ans[i] = max([ans[j] + ans[i-j] for j in range(0,i)])로 표현가능
