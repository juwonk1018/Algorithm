def solution(storey):
    answer = float("INF")
    def getZero(number, count):
        nonlocal answer
        
        if(number == 0):
            answer = min(answer, count)
            
        elif(number == 1):
            answer = min(answer, count+1)
            
        else:
            getZero((number - number%10)//10, count + number%10)
            getZero((number + 10 - number%10)//10, count + 10 - number%10)
    
    getZero(storey, 0)
    
    return answer