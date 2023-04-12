from collections import defaultdict
def solution(k, tangerine):
    num = defaultdict(int)
    for size in tangerine:
        num[size-1] += 1
    
    m = len(tangerine) - k
    
    result = []
    for item in num:
        if(num[item] <= m):
            result.append(num[item])
    
    result.sort(reverse=True)
    
    cnt = 0
    while(m != 0):
        if(result == []):
            break
        cur = result.pop()
        if(m >= cur):
            m -= cur
            cnt +=1
            
    return len(num) - cnt