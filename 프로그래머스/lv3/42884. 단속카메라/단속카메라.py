def solution(routes):
    routes.sort()
    
    startPoint, endPoint = -30001, -30001
    answer = 0
    for start, end in routes:
        if(startPoint <= start <= endPoint):
            startPoint = start
            endPoint = min(endPoint, end)
        else:
            answer += 1
            startPoint, endPoint = start, end
    
    return answer