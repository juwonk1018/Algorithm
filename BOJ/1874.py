import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]
stack = []
ans = []

for i in range(1,n+1):
    stack.append(i)
    ans.append("+")
    while(stack[-1] == arr[0]):
        arr.pop(0)
        stack.pop()
        ans.append("-")
        if(not arr or not stack):
            break
        
if(arr):
    print("NO")
else:
    print(*ans, sep='\n')

