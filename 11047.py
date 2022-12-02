import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split())

arr = []
temp = 0
cnt = 0

for i in range(n):
    arr.append(int(input().strip()))
    if(k >= arr[i]):
        temp = i


while(k!=0):
    if(k>=arr[temp]):
        cnt += int(k//arr[temp])
        k -= int((k//arr[temp]) * arr[temp])
        
    temp -= 1

print(cnt)



# for x in reversed(arr) 등 사용 가능, [
# arr = [int(input()) for _ in range(n)]로 표기 가능
