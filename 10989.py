import sys
input = sys.stdin.readline
num = [0]*10001
n = int(input().strip())
for _ in range(n):
    num[int(input().strip())]+=1

for i in range(1,10001):
    for j in range(num[i]):
        print(i)
