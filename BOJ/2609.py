import sys
input = sys.stdin.readline
a,b = map(int, input().strip().split())
tempa = a
tempb = b

while(a!=b):
    if(a>b):
        a-=b
    else:
        b-=a

print(a, tempa//a * tempb//a * a)
