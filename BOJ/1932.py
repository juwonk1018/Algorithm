n = int(input())
sum = []
arr = []
for i in range(1,n+1):
    sum.append([0] * i)
    arr.append(list(map(int,input().split())))

sum[0][0] = arr[0][0]
for i in range(1,n):
    for j in range(0,i+1):
        if(j==0):
            sum[i][j] = sum[i-1][j] + arr[i][j]
        elif(j==i):
            sum[i][j] = sum[i-1][j-1] + arr[i][j]
        else:
            sum[i][j] = max(sum[i-1][j-1] + arr[i][j], sum[i-1][j] + arr[i][j])
print(max(sum[n-1]))