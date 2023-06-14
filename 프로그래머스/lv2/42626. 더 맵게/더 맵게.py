import heapq
def solution(scoville, K):
    n = len(scoville)
    notSpicy = []
    canMake = False
    for i in range(n):
        if(scoville[i] < K):
            notSpicy.append(scoville[i])
        else:
            canMake = True
            
    heapq.heapify(notSpicy)
    answer = 0
    while(notSpicy):
        if(len(notSpicy) == 1):
            if(canMake):
                heapq.heappop(notSpicy)
                return answer + 1
            else:
                return -1
        
        l1 = heapq.heappop(notSpicy)
        l2 = heapq.heappop(notSpicy)
        newSpicy =  l1 + 2 * l2 
        if(newSpicy < K):
            heapq.heappush(notSpicy, newSpicy)
        else:
            canMake = True
        
        answer += 1
    return answer