def solution(board):
    n, m = len(board), len(board[0])
         
    l, r = 0, min(n,m)
    
    for i in range(n):
        for j in range(m):
            if(j>0 and board[i][j]):
                board[i][j] = board[i][j-1] + 1
                
    
    while(l<=r):
        print(l,r)
        mid = (l+r)//2
        
        isSquare = False
        for i in range(n):
            if(isSquare):
                break
            for j in range(m):
                if(isSquare):
                    break
                if(board[i][j] >= mid):
                    if(i+mid-1 < n):
                        for k in range(mid):
                            if(board[i+k][j] < mid):
                                break
                        else:
                            isSquare = True
        
        if(isSquare):
            l = mid + 1
        else:
            r = mid - 1
    
    
    answer = (l-1)**2
    
    return answer