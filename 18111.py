import sys
input = sys.stdin.readline
n,m,b = map(int, input().strip().split())
arr = []
total = 0
ans = float("inf")
minimum = float("inf")
ans2 = 0
for i in range(n):
    temp = list(map(int, input().strip().split()))
    minimum = min(minimum,min(temp))
    total += sum(temp)
    arr.append(temp)

for i in range(minimum,(total+b)//(m*n)+1):
    time = 0
    for j in range(n):
        for k in range(m):
            if(arr[j][k] > i):
                time += (arr[j][k] - i) * 2
                b += 1
            elif(arr[j][k] < i):
                b -= 1
                time += (i - arr[j][k])
    if(time < ans or (time == ans and i>ans2)):
        ans = time
        ans2 = i

print(ans, ans2)
                
        

