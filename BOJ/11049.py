import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n): #input
    arr.append(list(map(int, input().split())))

ans = [[float("inf")] * (n+1) for _ in range(n)] # ans[0][2]는 0부터 2까지의 최소 cost

for i in range(n):
    ans[i][i] = 0


for step in range(1, n):
    for i in range(n - step):
        for j in range(i, i+step):
            ans[i][i+step] = min(ans[i][i+step], ans[i][j] + ans[j+1][i+step]
                                 + arr[i][0] * arr[j][1] * arr[i+step][1])
print(ans[0][n-1])


#while을 for로 바꾸고 j에서 range(n-step+1)을 (i, i+step)으로 바꾸니 해결
#while이 for보다 더 느린가