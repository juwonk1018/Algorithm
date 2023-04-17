def solution(n, left, right):
    arr = []
    for i in range(n):
        if((i+1)*n-1 < left):
            continue
            
        for j in range(n):
            if(left <= i*n+j <= right):
                if(j <= i):
                    arr.append(i+1)
                else:
                    arr.append(j+1)
        
            if(i*n+j > right):
                return arr
    return arr