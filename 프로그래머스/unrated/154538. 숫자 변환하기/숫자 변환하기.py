def solution(x, y, n):
    result = set([x])
    
    answer = 0
    while(y not in result):
        nextResult = set()
        for num in result:
            for nextNumber in [num + n, num * 2, num * 3]:
                nextResult.add(nextNumber)
        result = nextResult
        
        if(min(result) > y):
            return -1
    
        answer += 1
    return answer