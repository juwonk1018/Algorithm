def solution(x, n):
    cur = x
    answer = []
    
    for i in range(n):
        answer.append(cur)
        cur += x
        
    
    return answer