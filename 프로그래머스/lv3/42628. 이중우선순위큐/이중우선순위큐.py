import heapq

# 테케가 모든 경우를 거르지 못하는데, insert하는 idx를 같이 heap에 넣어서 visited를 만드는 방식으로 문제 해결 가능

def solution(operations):
    maxHeap = []
    minHeap = []
    
    iCount = 0
    dCount = 0
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        
        if(op == 'I'):
            heapq.heappush(maxHeap, -num)
            heapq.heappush(minHeap, num)
            iCount += 1
            
        elif(op == 'D' and num == 1 and iCount > dCount and maxHeap):
            heapq.heappop(maxHeap)
            dCount += 1
        
        elif(op == 'D' and num == -1 and iCount > dCount and minHeap):
            heapq.heappop(minHeap)
            dCount += 1
        
        if(iCount == dCount):
            minHeap, maxHeap = [], []
    
    if(iCount > dCount):
        return [-heapq.heappop(maxHeap), heapq.heappop(minHeap)]
    
    else:
        return [0,0]
    