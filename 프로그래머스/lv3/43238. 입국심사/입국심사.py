# 최대한 비는 시간 없이 심사
import heapq

def solution(n, times):
    start, end = 1, 10**18
    
    while(start < end):
        
        mid = (start + end) // 2
        num = 0
        for time in times:
            num += (mid//time)
        if(num >= n):
            end = mid
        else:
            start = mid + 1
        
    print(start)
    answer = start
    return answer