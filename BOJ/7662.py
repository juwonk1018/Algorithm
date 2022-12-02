import sys
import heapq
from collections import deque


input = sys.stdin.readline

test = int(input())


for _ in range(test):
    k = int(input())
    max_queue = []
    min_queue = []

    visited = [0] * 1000001

    for i in range(k):
        command, num = input().split()
        num = int(num)
        if(command == "I"):
            heapq.heappush(max_queue, (-num, i))    
            heapq.heappush(min_queue, (num, i))
        elif(command == "D"):
            
            if(num == 1):
                if(len(max_queue) == 0):
                    continue
                value, idx = heapq.heappop(max_queue)
                while(max_queue and visited[idx] == 1):
                    value, idx = heapq.heappop(max_queue)
                visited[idx] = 1
            
            elif(num == -1):
                if(len(min_queue) == 0):
                    continue
                value, idx = heapq.heappop(min_queue)
                while(min_queue and visited[idx] == 1):
                    value, idx = heapq.heappop(min_queue)
                visited[idx] = 1

    if(len(max_queue) == 0 or len(min_queue) == 0):
        print("EMPTY")
    else:
        value, idx = heapq.heappop(min_queue)
        while(min_queue and visited[idx] == 1):
            value, idx = heapq.heappop(min_queue)
        value2, idx2 = heapq.heappop(max_queue)
        while(max_queue and visited[idx2] == 1):
            value2, idx2 = heapq.heappop(max_queue)
        
        if(visited[idx] == 1):
            print("EMPTY")
        else:
            print(-value2, value)


#min_heap, max_heap 두개를 이용해, index를 가지고 제거한 항목을 알려줌.
#heapq에서 가장 작은 값의 index는 0