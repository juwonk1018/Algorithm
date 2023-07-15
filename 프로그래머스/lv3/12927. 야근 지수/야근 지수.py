from collections import deque
def solution(n, works):
    l = len(works)
    
    works = works + [0]
    works.sort(reverse = True)
    
    cur = 0
    
    while(n):
        
        while(cur < l-1 and works[cur] == works[cur+1]):
            cur += 1
        
        if(cur == l-1): # 모두 같은 작업량일 때
            s = 0
            
            minusNumber = min(n//l, works[cur])
            
            for i in range(l):
                works[i] -= minusNumber
                s += minusNumber
            n -= s
                
            if(sum(works) > 0):
                for i in range(min(n,l)):
                    works[i] -= 1
                    n -= 1
            else:
                n = 0
            
        else:
            diff = works[cur] - works[cur+1]
            
            for i in range(cur+1):
                if(n==0):
                    break
                works[i] -= 1
                n -= 1
            
    answer = 0
    for i in range(l):
        answer += works[i]**2
    return answer