import sys
input = sys.stdin.readline
n = int(input().strip())

fi = [1,0,0,1] + [0] * 80

for i in range(2,41):
    fi[2*i] = fi[2*i-2] + fi[2*i-4]
    fi[2*i+1] = fi[2*i-1] + fi[2*i-3]
       
for i in range(n):
    num = int(input().strip())
    print(*fi[2*num:2*num+2])

