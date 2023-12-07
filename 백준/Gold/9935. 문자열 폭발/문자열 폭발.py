import sys
from collections import deque
input = sys.stdin.readline

inp = input().strip()
boom = input().strip()

substr = [list(boom[:i]) for i in range(1,len(boom))]
idx = 0

result = []
storage = deque()
for i in range(len(inp)):
    result.append(inp[i])

    if(inp[i] == boom[0]):
        if(len(boom) == 1):
            result.pop()
            continue
        if(idx != 0):
            storage.appendleft(idx)
            idx = 0
        idx += 1
        
    elif(inp[i] == boom[idx]):
        if(idx != len(boom) - 1):
            idx += 1
        else:
            idx = 0
            if(storage):
                idx = storage.popleft()
            for _ in range(len(boom)):
                result.pop()
    else:
        storage = deque()
        idx = 0
        

result = "".join(result)

if(result == ""):
    print("FRULA")
else:
    print(result)
