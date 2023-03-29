
def solution(grid):
    dxdy = [[1,0],[0,1],[-1,0],[0,-1]] # 아래, 오른, 위, 왼
    
    def cycleCheck(ii, jj, kk):
        cur = [ii,jj,kk]
        cnt = 0
        while(True):
            i, j, k = cur
            check[i][j][k] = 1
            
            x, y, d = (i+dxdy[k][0])%len(grid), (j+dxdy[k][1])%len(grid[0]), k
            
            if(grid[x][y] == 'L'):
                d = (d+1)%4
            elif(grid[x][y] == 'R'):
                d = (d-1)%4
                
#             if(grid[i][j] == 'S'):
#                 cur = [i+dxdy[k][0], j+dxdy[k][1], k]

#             elif(grid[i][j] == 'L'):
#                 cur = [i+dxdy[(k+1)%4][0], j+dxdy[(k+1)%4][1], (k+1)%4]

#             elif(grid[i][j] == 'R'):
#                 cur = [i+dxdy[(k-1)%4][0], j+dxdy[(k-1)%4][1], (k-1)%4]
                
#             cur[0] = cur[0] % len(grid)
#             cur[1] = cur[1] % len(grid[0])
            
            cnt += 1
            
            cur = [x,y,d]
            if(check[cur[0]][cur[1]][cur[2]]):
                if(cur[0] == ii and cur[1] == jj and cur[2] == kk):
                    return cnt
                else:
                    return -1
            
        
    answer = []
    
    check = [[[0,0,0,0] for _ in range(len(grid[0]))] for _ in range(len(grid))] # 아래, 오른, 위, 왼
             
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if(check[i][j][k] == 0):
                    ans = cycleCheck(i,j,k)
                    if(ans):
                        answer.append(ans)
                    
    answer.sort()
    return answer