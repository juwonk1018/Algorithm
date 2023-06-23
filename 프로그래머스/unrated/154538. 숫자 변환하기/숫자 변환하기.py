def solution(x, y, n):
    result = set([x])
    
    answer = 0
    while(y not in result):
        nextResult = set()
        for num in result:
            nextResult.add(num + n)
            nextResult.add(num * 2)
            nextResult.add(num * 3)
        result = nextResult
        
        if(min(result) > y):
            return -1
    
        answer += 1
    return answer