import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []

for i in range(666,2700000):
    if('666' in str(i)):
        arr.append(i)

print(arr[n-1])
