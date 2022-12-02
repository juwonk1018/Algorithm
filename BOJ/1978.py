import sys
input = sys.stdin.readline

N = input().strip()
arr = [0]*1001
arr[1] = 1
for i in range(2,1000):
    if(arr[i] == 0):
        for j in range(i+1,1001):
            if(j%i==0):
                arr[j] = 1

ans = 0


for i in list(map(int,input().strip().split())):
    if(arr[i] == 0):
        ans+=1
        
print(ans)
