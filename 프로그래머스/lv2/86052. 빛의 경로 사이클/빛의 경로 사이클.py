
            
def solution(grid):
    
    def cycleCheck(ii, jj, kk):
        cur = [ii,jj,kk]
        cnt = 0
        while(True):
            i, j, k = cur
            check[i][j][k] = 1
            if(grid[i][j] == 'S'):
                if(k==0):
                    cur = [i+1, j, 0]
                elif(k==1):
                    cur = [i, j+1, 1]
                elif(k==2):
                    cur = [i, j-1, 2]
                elif(k==3):
                    cur = [i-1, j, 3]

            elif(grid[i][j] == 'L'):
                if(k==0):
                    cur = [i, j+1, 1]
                elif(k==1):
                    cur = [i-1, j, 3]
                elif(k==2):
                    cur = [i+1, j, 0]
                elif(k==3):
                    cur = [i, j-1, 2]

            elif(grid[i][j] == 'R'):
                if(k==0):
                    cur = [i, j-1, 2]
                elif(k==1):
                    cur = [i+1, j, 0]
                elif(k==2):
                    cur = [i-1, j, 3]
                elif(k==3):
                    cur = [i, j+1, 1]

            cur[0] = cur[0] % len(grid)
            cur[1] = cur[1] % len(grid[0])
            
            cnt += 1
            
            if(check[cur[0]][cur[1]][cur[2]]):
                if(cur[0] == ii and cur[1] == jj and cur[2] == kk):
                    return cnt
                else:
                    return -1
            
        
    answer = []
    
    check = [[[0,0,0,0] for _ in range(len(grid[0]))] for _ in range(len(grid))] # U, L, R, D
             
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if(check[i][j][k] == 0):
                    ans = cycleCheck(i,j,k)
                    if(ans):
                        answer.append(ans)
                    
    answer.sort()
    return answer