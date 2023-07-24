def solution(A, B):
    B.sort()
    cur = 0; n = len(B)
    answer = 0
    
    for a in sorted(A):
        if(cur >= n):
            break
        
        while(cur < n-1 and B[cur] <= a):
            cur += 1
        
        if(B[cur] > a):
            answer += 1
            cur += 1
    
    return answer