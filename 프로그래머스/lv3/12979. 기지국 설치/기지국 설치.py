def solution(n, stations, w):
    lastStation = -w
    
    answer = 0
    for station in stations:
        diff = station - lastStation - 2 * w - 1
        if(diff > 0):
            answer += 1 + (diff - 1) // (2*w+1)
        
        print(answer)
        lastStation = station
        
    diff = n - lastStation - w
    if(diff > 0):
        answer += 1 + (diff - 1) // (2*w+1)
    return answer