import sys
input = sys.stdin.readline

num = list(map(int,input().strip().split()))
dup = num.copy()
dup.sort()

if(num == dup):
    print("ascending")
elif(num == list(reversed(dup))):
    print("descending")
else:
    print("mixed")
