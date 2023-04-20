from collections import deque
def solution(cacheSize, cities):
    cache = deque() * cacheSize
    
    answer = 0
    
    if(cacheSize == 0):
        return 5*len(cities)
    
    for city in cities:
        lower_city = city.lower()
        if(lower_city in cache): # Cache Hit, 시간을 1 추가
            answer += 1
            del cache[cache.index(lower_city)]
            cache.append(lower_city)
        else: # Cache Miss
            answer += 5
            if(len(cache) == cacheSize):
                cache.popleft()
            cache.append(lower_city)
    
    return answer