import sys
input = sys.stdin.readline
ans = [100,100,200,200,300,300,400,400,500]
arr = list(map(int,input().strip().split()))
sum = 0
flag = 0
for i in range(len(arr)):
    sum += int(arr[i])
    if(arr[i] > ans[i]):
        print("hacker")
        flag = 1
        break

if(flag ==0):
    if(sum >= 100):
        print("draw")
    else:
        print("none")
    
