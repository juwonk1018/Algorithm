# 16:18

def solution(places):
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    dx2 = [2,1,0,-1,-2,-1,0,1]
    dy2 = [0,-1,-2,-1,0,1,2,1]
    
    def safeCheck(place, x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(0 <= nx < 5 and 0 <= ny < 5):
                if(place[nx][ny] == "P"):
                    return False
    
        for i in range(8):
            nx = x + dx2[i]
            ny = y + dy2[i]
            
            if(0 <= nx < 5 and 0 <= ny < 5):
                if(place[nx][ny] == "P"):
                    if(x == nx and y != ny and place[nx][max(y,ny)-1] == "O"):
                        return False
                    
                    elif(x != nx and y == ny and place[max(x,nx)-1][ny] == "O"):
                        return False
                    
                    elif(x != nx and y != ny and (place[nx][y] == "O" or place[x][ny] == "O")):
                        return False
                
        return True
    
    answer = []
    
    for place in places:
        allSafe = 1
        for i in range(5):
            for j in range(5):
                if(place[i][j] == 'P'):
                    if(safeCheck(place, i, j) == False):
                        allSafe = 0
        
        answer.append(allSafe)
                        
    return answer