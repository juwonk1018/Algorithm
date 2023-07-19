def solution(arr):
    n = len(arr)
    
    def quadPress(startX, endX, startY, endY):

        midX = (startX + endX) // 2
        midY = (startY + endY) // 2
        
        cycleList = [[startX, midX, startY, midY], [midX + 1, endX, startY, midY], [startX, midX, midY+1, endY], [midX+1, endX, midY+1, endY]]

        
        for sx, ex, sy, ey in cycleList:
            if(sx==ex and sy==ey):
                answer[arr[sx][sy]] += 1
            
            else:
                base = arr[sx][sy]
                check = False
                for i in range(sx, ex+1):
                    for j in range(sy,ey+1):
                        if(base != arr[i][j]):
                            check = True

                if(check):
                    quadPress(sx, ex, sy, ey)
                else:
                    answer[base] += 1

    answer = [0, 0]
    
    num = [0, n**2]
    
    for i in range(len(num)):
        if(sum(map(sum, arr)) == num[i]):
            answer[i] += 1
            return answer
               
    quadPress(0, n-1, 0, n-1)
    return answer