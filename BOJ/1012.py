import sys
input = sys.stdin.readline


for i in range(int(input().strip())):
    ans = 0
    m,n,k = map(int,input().strip().split())
    arr = [[0]*m for _ in range(n)]
    
    for l in range(k):
        x,y = map(int,input().strip().split())
        arr[y][x] = 1
    for y in range(n):
        for x in range(m):
            if(arr[y][x]==1):
                stack = []
                arr[y][x] = 0
                stack.append([y,x])
                while(stack):
                    ny, nx = stack.pop(0)
                    if(ny<n-1):
                        if(arr[ny+1][nx] == 1):
                            arr[ny+1][nx] = 0
                            stack.append([ny+1,nx])
                    if(ny>0):
                        if(arr[ny-1][nx] == 1):
                            arr[ny-1][nx] = 0
                            stack.append([ny-1,nx])
                    if(nx<m-1):
                        if(arr[ny][nx+1] == 1):
                            arr[ny][nx+1] = 0
                            stack.append([ny,nx+1])
                    if(nx>0):
                        if(arr[ny][nx-1] == 1):
                            arr[ny][nx-1] = 0
                            stack.append([ny,nx-1])
                ans+=1
    print(ans)
                

