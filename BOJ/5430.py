import sys
from collections import deque
n = int(input())
for _ in range(n):
    str = sys.stdin.readline().strip()
    num = int(sys.stdin.readline())
    temp = sys.stdin.readline().strip()[1:-1]
    err = False
    arr = deque(temp.split(","))
    if(arr[0]==''):
        arr = []
    
    reversed = False
    for j in range(len(str)):
        if(str[j] == 'R'):
            reversed = not(reversed)
        if(str[j] == 'D'):
            if(len(arr) > 0):
                if(reversed):
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print("error")
                err = True
                break
    if(reversed):
        arr.reverse()
    
    if(not(err)):
        print("[" + ",".join(list(arr)) + "]")

'''
꼭 reverse 할 필요는 없음
'''