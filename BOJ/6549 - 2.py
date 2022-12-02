import sys
input = sys.stdin.readline


while(True):

    arr = list(map(int, input().split()))
    n = arr.pop(0)
    
    if(n == 0):
        break

    stack = []
    result = 0

    for i in range(n):        
        while(len(stack) != 0 and arr[i] < arr[stack[-1]]):
            temp = stack.pop()
            if(len(stack) == 0):
                result = max(arr[temp] * i, result)
            else:
                result = max(arr[temp] * (i - stack[-1] - 1), result)
            #stack의 마지막 index를 포함하지 않고 i도 포함하지 않아 i - stack[-1] - 1
        
        stack.append(i)

    while(len(stack) != 0):
        temp = stack.pop()
        
        if(len(stack) == 0):
            result = max(result, arr[temp] * n)
        else:
            result = max(result, arr[temp] * (n - 1 - stack[-1])) # 사실상 -(stack[-1] + 1)
    
    print(result)
