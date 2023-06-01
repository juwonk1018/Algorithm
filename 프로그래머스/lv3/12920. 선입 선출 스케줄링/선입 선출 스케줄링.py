def solution(n, cores):
    
    left, right = 0, 10000000000
    while(left <= right):
        mid = (left + right) // 2
        totalWork = 0
        for time in cores:
            totalWork += mid // time + 1
        
        if(totalWork >= n):
            right = mid - 1
        else:
            left = mid + 1
            
    left = left - 1
    if(left >= 0):
        for time in cores:
            n -= left//time + 1
            
    for i in range(len(cores)):
        if((left+1) % cores[i] == 0):
            n -= 1
        
        if(n == 0):
            return i+1
            