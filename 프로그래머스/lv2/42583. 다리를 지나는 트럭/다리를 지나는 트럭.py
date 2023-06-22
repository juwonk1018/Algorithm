from collections import deque
def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    
    bridge = deque([0] * bridge_length)
    bridgeWeight = 0
    cur = 0
    answer = 0
    
    while(cur != n):
        bridgeWeight -= bridge.pop()
        if(bridgeWeight + truck_weights[cur] <= weight):
            bridgeWeight += truck_weights[cur]
            bridge.appendleft(truck_weights[cur])
            cur += 1
        else:
            bridge.appendleft(0)
            
        answer += 1
    
    while(bridgeWeight):
        bridgeWeight -= bridge.pop()
        answer += 1
        
    return answer