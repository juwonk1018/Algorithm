def solution(number, k):
    s = []
    target = len(number) - k
    for char in number:
        if(s == []):
            s.append(char)
        
        else:
            while(s and k and char > s[-1]):
                s.pop()
                k -= 1
            
            s.append(char)
                
    answer = ''.join(s)[:target]
        
    return answer