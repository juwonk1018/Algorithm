from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    position = deque([i for i in range(len(priorities))])
    
    answer = 1
    while(priorities):
        cur = priorities.popleft()
        pos = position.popleft()
        
        if(priorities):
            if(max(priorities) <= cur):
                
                if(pos == location):
                    return answer
                answer += 1
            else:
                priorities.append(cur)
                position.append(pos)
            
    return answer