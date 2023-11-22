from collections import Counter, defaultdict
import heapq
def solution(gems):
    
    n = len(gems)
    sortNumber = len(set(gems))
    
    answer = []
    gemCount = defaultdict(int)
    
    start, end = 0, 0
    
    gemCount[gems[start]] += 1
    
    while(True):
        if(start >= n or end >= n):
            break
            
        if(len(gemCount) < sortNumber):
            end += 1
            if(end < n):
                gemCount[gems[end]] += 1
        
        elif(len(gemCount) == sortNumber):
            heapq.heappush(answer, [end-start, start, end])
            
            gemCount[gems[start]] -= 1
            if(gemCount[gems[start]] == 0):
                del gemCount[gems[start]]
                
            start += 1
            
            if(end < start):
                end = start
            
        
            
        
        
    return [answer[0][1]+1, answer[0][2]+1]