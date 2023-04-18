def solution(board, aloc, bloc):
    X, Y = len(board), len(board[0])
    dxdy = [[1,0], [-1,0], [0,1], [0,-1]]
    
    
    def move(board, count, aloc, bloc):
        ax, ay = aloc[0], aloc[1]
        bx, by = bloc[0], bloc[1]
        
        if(board[ax][ay] == 0):
            return [False, count] # B가 이김
            
        if(board[bx][by] == 0):
            return [True, count]
        
        #경로에 이길 방법이 존재한다면, 최단 경로가 존재하는 방향으로 이동
        #경로에 이길 방법이 존재하지 않는다면, 최장 경로가 존재하는 방향으로 이동
        
        canWin = False
        canMove = False
        maxCount = 0; minCount = float("INF")
        
        if(count%2 == 0): # A의 움직임    
            for dx, dy in dxdy:
                nx, ny = ax + dx, ay + dy
                if(0 <= nx < X and 0 <= ny < Y and board[nx][ny] == 1):
                    canMove = True
                    
                    board[ax][ay] = 0
                    result = move(board, count + 1, [nx, ny], bloc)    
                    board[ax][ay] = 1
                    
                    if(result[0] == True):
                        canWin = True
                        minCount = min(minCount, result[1])
                    else:
                        maxCount = max(maxCount, result[1])
                        
            if(not(canMove)):
                return [False, count]
            
            if(canWin): # 이길 가능성이 존재한다면
                return [True, minCount]
            else:
                return [False, maxCount]
                        
            
            
        else: # B의 움직임
            for dx, dy in dxdy:
                nx, ny = bx + dx, by + dy
                if(0 <= nx < X and 0 <= ny < Y and board[nx][ny] == 1):
                    canMove = True
                    
                    board[bx][by] = 0
                    result = move(board, count + 1, aloc, [nx, ny])
                    board[bx][by] = 1
                    
                    if(result[0] == True):
                        maxCount = max(maxCount, result[1])
                    else:
                        canWin = True
                        minCount = min(minCount, result[1])
                        
            if(not(canMove)):
                return [True, count]
            
            if(canWin):
                return [False, minCount]
            else:
                return [True, maxCount]
                  
    ans = move(board, 0, aloc, bloc)
    print(ans)
    return ans[1]