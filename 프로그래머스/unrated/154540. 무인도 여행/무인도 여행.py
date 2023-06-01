from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def solution(maps):
    def BFS(x, y):
        foodAmount = 0
        q = deque()
        
        def changeMap(posX, posY):
            food = int(maps[posX][posY])
            maps[posX][posY] = 'X'
            q.append([posX,posY])
            
            return food
        
        foodAmount += changeMap(x,y)
        
        while(q):
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dy[i], cy + dx[i]
                if(0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X'):
                    foodAmount += changeMap(nx,ny)
                    
        return foodAmount
        
    maps = list(map(list, maps))
    n, m = len(maps), len(maps[0])
    answer = []
    
    for i in range(n):
        for j in range(m):
            if(maps[i][j] != "X"):
                answer.append(BFS(i, j))
    
    answer.sort()
    return answer if answer else [-1]