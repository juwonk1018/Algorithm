import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [[0] * (n+1) for _ in range(n+1)]
m = int(input())

for i in range(n): #홀수
    for j in range(n):
        if(i-j<0 or i+j>=n):
            break

        if(arr[i+j] == arr[i-j]):
            ans[i-j][i+j] = 1
        else:
            break

for i in range(n):
    start = i
    end = i+1
    
    
    for j in range(n):
        if(end >= n or start < 0):
            break

        if(arr[start] == arr[end]):
            ans[start][end] = 1
            start -= 1
            end +=1
        else:
            break

        


for _ in range(m):
    s, e = map(int, input().split())
    print(ans[s-1][e-1])


# a부터 b까지가 palindrome인 것을 판별하기 위해, a+1부터 b-1까지가 palinedrome이고 a,b가 같다는 것을 이용한 DP도 사용가능