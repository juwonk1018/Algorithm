n = int(input())
ans = [' '*(2*n)] * n

ans[0] = ans[0][:n-1] + '*' + ans[0][n:]
ans[1] = ans[1][:n-2] + '* *' + ans[1][n+1:]
ans[2] = ans[2][:n-3] + '*****' + ans[2][n+2:]
    

def makePattern(row, col, width, height):
    for i in range(height):
        ans[row+height+i] = ans[row+height+i][:col-width//2-1-width//2] + ans[row+i][col-width//2:col+width//2+1] + ans[row+height+i][col-width//2-1+width//2+1:]
    for i in range(height):
        ans[row+height+i] = ans[row+height+i][:col+width//2+1-width//2] + ans[row+i][col-width//2:col+width//2+1] + ans[row+height+i][col+width//2+1+width//2+1:]
    

height = 3
while(height < n):
    makePattern(0, n-1, height * 2 - 1, height)
    height *= 2
    
for i in range(n):
    print(ans[i])