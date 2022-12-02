from collections import deque

n = int(input())
arr = []
ans = [[0] * n for _ in range(n)]
for _ in range(n):
    arr.append(input().strip())


count = 0
countRG = 0

while(True):
    
    queue = deque()
    for i in range(n):
        for j in range(n):
            if(ans[i][j] == 0):
                queue.append([i,j])
                break
        if(queue != deque([])): break
    if(queue == deque([])):
        break
    
    color = arr[queue[0][0]][queue[0][1]]
    while(queue):
        element = queue.popleft()
        ans[element[0]][element[1]] = 1
        for x,y in [[-1,0],[0,-1],[1,0],[0,1]]:
            dx = element[0] + x
            dy = element[1] + y
            if(0<= dx and dx < n and 0<= dy and dy < n):
                if(arr[dx][dy] == color and ans[dx][dy] == 0):
                    ans[dx][dy] = 1
                    queue.append([dx,dy])
    count +=1

for i in range(n):
    arr[i] = arr[i].replace('G','R')

ans = [[0] * n for _ in range(n)]


while(True):
    queue = deque()
    for i in range(n):
        for j in range(n):
            if(ans[i][j] == 0):
                queue.append([i,j])
                break
        if(queue != deque([])): break
    if(queue == deque([])):
        break
    
    color = arr[queue[0][0]][queue[0][1]]
    while(queue):
        element = queue.popleft()
        ans[element[0]][element[1]] = 1
        for x,y in [[-1,0],[0,-1],[1,0],[0,1]]:
            dx = element[0] + x
            dy = element[1] + y
            if(0<= dx and dx < n and 0<= dy and dy < n):
                if(arr[dx][dy] == color and ans[dx][dy] == 0):
                    ans[dx][dy] = 1
                    queue.append([dx,dy])
    countRG +=1

print(count, countRG)

    

"""
[0] * n for _ in range(n) 을 하면 값이 다 copy
"""