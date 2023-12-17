import sys

input = sys.stdin.readline

n = int(input())

SK = [0] * (n+1)

SK[1] = 1

for i in range(n+1):
    for j in [i-2, i-4, i-6]:
        if(j > 0 and SK[j]):
            SK[i] = 1

if(SK[n]):
    print("SK")
else:
    print("CY")

 