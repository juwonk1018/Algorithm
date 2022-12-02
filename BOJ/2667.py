from collections import deque

n = int(input())
arr  =[list(map(int, input())) for _ in range(n)]

ans = []

for i in range(n):
    for j in range(n):
        if(arr[i][j] == 1):
            num = 1
            queue = deque()

            queue.append([i,j])
            arr[i][j] = 0
            while(queue):
                idx = queue.popleft()
                for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    idx_dx = idx[0] + dx
                    idx_dy = idx[1] + dy
                    if(0<= idx_dx and idx_dx < n and 0<= idx_dy and idx_dy < n):
                        if(arr[idx_dx][idx_dy] == 1):
                            num+=1
                            arr[idx_dx][idx_dy] = 0
                            queue.append([idx_dx,idx_dy])
            ans.append(num)        

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
