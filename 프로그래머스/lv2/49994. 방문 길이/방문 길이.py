def solution(dirs):
    dirList = ["L", "U", "R", "D"]
    dirMove = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    
    visited = [[[0, 0] for _ in range(11)] for _ in range(11)]
    
    moveDir = dict()
    for i in range(4):
        moveDir[dirList[i]] = dirMove[i]
        
    curPosition = [0,0]
    
    for direction in dirs:
        nextX, nextY = curPosition[0] + moveDir[direction][0], curPosition[1] + moveDir[direction][1]
        
        if(-5 <= nextX <= 5 and -5 <= nextY <= 5):
            dx = min(curPosition[0], nextX)
            dy = min(curPosition[1], nextY)
            if direction == "L" or direction == "R":
                visited[dx][dy][1] = 1
                print(dx,dy,1)
            else:
                visited[dx][dy][0] = 1
                print(dx,dy,0)
                
            curPosition = [nextX, nextY]
            
    answer = 0
    for i in range(11):
        answer += sum(list(map(sum, visited[i])))
    
    return answer