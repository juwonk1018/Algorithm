from collections import defaultdict

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    
    s1 = defaultdict(int)
    s2 = defaultdict(int)
    
    for i in range(len(str1)-1):
        if(str1[i].isalpha() and str1[i+1].isalpha()):
            s1[str1[i:i+2]] += 1
            
    for i in range(len(str2)-1):
        if(str2[i].isalpha() and str2[i+1].isalpha()):
            s2[str2[i:i+2]] += 1
        
    numerator, denominator = 0, 0
    for s in s1:
        if(s in s2):
            numerator += min(s1[s], s2[s])
            denominator += max(s1[s], s2[s])
        else:
            denominator += s1[s]
        
    for s in s2:
        if(s not in s1):
            denominator += s2[s]
    
    print(numerator, denominator)
    if(numerator == 0 and denominator == 0):
        answer = 65536
    else:
        answer = int((numerator/denominator)*65536)
    return answer