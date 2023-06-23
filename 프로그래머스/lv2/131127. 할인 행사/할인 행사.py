def solution(want, number, discount):
    n = len(want)
    answer = 0
    num = [0] * n
    idx = dict()
    
    for i in range(n):
        idx[want[i]] = i
    
    for i in range(len(discount)):
        if(discount[i] in want):
            num[idx[discount[i]]] += 1
                
        if(i >= 10):
            if(discount[i-10] in want):
                num[idx[discount[i-10]]] -= 1
                
        if(num == number):
            answer += 1
        
    return answer