import sys
input = sys.stdin.readline

arr = [int(input()) for i in range(9)]
s = sum(arr)

answer = []
for i in range(9):
    for j in range(i+1, 9):
        if(arr[i] + arr[j] == s-100):
            answer = list(set(arr) - set([arr[i], s-100-arr[i]]))
            break

for i in list(sorted(answer)):
    print(i)