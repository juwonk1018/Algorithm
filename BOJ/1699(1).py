import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [0]*100001
arr[1] = 1
arr[2] = 2
arr[3] = 3
arr[4] = 1

for i in range(1,n+1):
    sol = []
    for j in range(1,int(i**(1/2))+1):
        sol.append(arr[i - j**2] + 1)
    arr[i] = min(sol)

print(arr[n])
