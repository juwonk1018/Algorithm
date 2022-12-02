import sys
input = sys.stdin.readline
arr = list(map(int, input().strip().split()))
print(min(arr[2]-arr[0],arr[0],arr[3]-arr[1],arr[1]))

#x,y,w,h=map(int,input().split()), print(min(x,w-x,y,h-y))
