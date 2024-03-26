def solution(board):
    
    
    # for i in range(1, len(b)) :
    #     for j in range(1, len(b[0])):
    #         if b[i][j] >= 1 :
    #             b[i][j] += min(b[i-1][j-1],b[i][j-1],b[i-1][j])
                
    
                
                
    n, m = len(board), len(board[0])
         
    l, r = 0, min(n,m)
    
    for i in range(n):
        for j in range(m):
            if(j>0 and board[i][j]):
                board[i][j] = board[i][j-1] + 1
                
    
    while(l<=r):
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