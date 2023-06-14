def solution(elements):
    n = len(elements)
    
    answer = set()
    
    for i in range(n):
        cur = elements[i:] + elements[:i]
        for j in range(1, n):
            cur[j] += cur[j-1]
        
        answer |= set(cur)
    
    return len(answer)