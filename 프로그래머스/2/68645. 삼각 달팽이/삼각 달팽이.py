def solution(n):
    answer = [[0] * i for i in range(1,n+1)]
    
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    x, y, mode = 0, 0, 0
    cur = 1
    
    end = n*(n+1)//2
    while(cur <= end):
        answer[x][y] = cur
        
        nx, ny = x + dx[mode], y + dy[mode]
        if(not(0 <= nx < n and 0 <= ny <= nx) or answer[nx][ny] != 0):
            mode = (mode + 1) % 3
            nx, ny = x + dx[mode], y + dy[mode]
            
        x, y = nx, ny
        if(not(0 <= x < n and 0 <= y <= x)):
            break
            
        cur += 1
    
    answerList = []
    for i in answer:
        answerList += i
    return answerList
