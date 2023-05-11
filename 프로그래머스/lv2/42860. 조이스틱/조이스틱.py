def solution(name):
    n = len(name)
    
    def BFS(position, cur):
        
        if(position == []):
            return 0
        
        smallIdx, largeIdx = -1, -1
        
        if(cur in position):
            smallIdx, largeIdx = cur, cur
        else:
            for i in range(n):
                if((cur + i) % n in position):
                    largeIdx = (cur + i) % n
                    break
                    
            for i in range(n):
                if((cur - i) % n in position):
                    smallIdx = (cur - i) % n
                    break
            
        minValue = float("INF")
        dist = min(abs(cur - largeIdx), n - abs(cur - largeIdx))
        minValue = min(minValue, dist + BFS(position[:position.index(largeIdx)] + position[position.index(largeIdx)+1:], position[position.index(largeIdx)]))
        
        if(largeIdx != smallIdx):
            dist = min(abs(cur - smallIdx), n - abs(cur - smallIdx))
            minValue = min(minValue, dist + BFS(position[:position.index(smallIdx)] + position[position.index(smallIdx)+1:], position[position.index(smallIdx)]))
                
        return minValue
    
    answer = 0
    changePosition = []
    for i in range(n):
        if(name[i] != 'A'):
            changePosition.append(i)
            answer += min(abs(ord(name[i]) - ord('A')), abs(ord("Z") + 1 - ord(name[i])))
        
    return answer + BFS(changePosition, 0)