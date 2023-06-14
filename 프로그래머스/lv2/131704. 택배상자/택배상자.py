def solution(order):
    container = [i for i in range(len(order), 0, -1)]
    tempContainer = []
    
    answer = 0
    for i in range(len(order)):
        cur = order[i]
        
        
        if(tempContainer and tempContainer[-1] == cur):
            answer += 1
            tempContainer.pop()
        
        else:
        
            while(container and container[-1] != cur):
                tempContainer.append(container.pop())

            if(container and container[-1] == cur):
                answer += 1
                container.pop()
            else:
                break
                
        
    return answer