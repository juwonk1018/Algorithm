import sys
n, m = map(int, input().split())

arr = list(map(int, input().split()))

psum = [0] * n

answer = 0
for i in range(n):
    if(i==0):
        psum[i] = arr[0] % m
    else:
        psum[i] = (psum[i-1] + arr[i])%m

    if(psum[i] == 0):
        answer += 1


count = [0] * m
for i in range(n):
    if(count[psum[i]]):
        answer += count[psum[i]]
    count[psum[i]] += 1

print(answer)
    