a = input().strip()
b = input().strip()

arr = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if(a[i-1] == b[j-1]):
            arr[i][j] = arr[i-1][j-1] + 1
        if(a[i-1] != b[j-1]):
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[-1][-1])



#DP 어려워~