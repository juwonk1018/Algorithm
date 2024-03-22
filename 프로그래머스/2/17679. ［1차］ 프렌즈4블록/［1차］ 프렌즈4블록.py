def solution(m, n, board):
    
    def playRound():
        cnt = 0
        removedBlock = set([])
        
        for i in range(1,n):
            for j in range(1,m):
                if(board[i][j] != '' and board[i][j] == board[i][j-1] == board[i-1][j] == board[i-1][j-1]):
                    removedBlock.add((i,j))
                    removedBlock.add((i,j-1))
                    removedBlock.add((i-1,j))
                    removedBlock.add((i-1,j-1))

        # 높은 위치의 블록부터 제거
        removedBlock = list(sorted(list(removedBlock), key =lambda x:[x[0],-x[1]])) 
        for i, j in removedBlock:
            board[i].pop(j)
            board[i].append('')
            cnt += 1
        
        if(cnt):
            nonlocal answer
            answer += cnt
            playRound()
    
    answer = 0
    board = [[board[i][j] for i in range(m)][::-1] for j in range(n)] # 각 column마다 높이가 아래에서 위로 증가하는 형태로 변경
    playRound()
    
    return answer