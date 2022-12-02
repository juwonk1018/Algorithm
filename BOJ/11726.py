import sys
input = sys.stdin.readline
number = int(input().strip())

arr = [0] * 1001
arr[1] = 1
arr[2] = 2

for i in range(number+1):
    if(arr[i] == 0):
        arr[i] = (arr[i-1] + arr[i-2])%10007

print(arr[number])
