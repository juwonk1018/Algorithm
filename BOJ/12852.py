from collections import deque
n = int(input())

ans = deque()
ans.append([n])

if(n == 1):
    print(0)
    print(1)
else:
    while(True):
        cur = ans.popleft()
        num = cur[-1]
        
        if(num % 2 == 0):
            if(num//2 == 1):
                print(len(cur))
                print(*cur + [1])
                break
            ans.append(cur + [num//2])
        if(num % 3 == 0):
            if(num//3 == 1):
                print(len(cur))
                print(*cur + [1])
                break
            ans.append(cur + [num//3])

        ans.append(cur + [num-1])
