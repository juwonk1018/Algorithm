from math import gcd

def solution(arrayA, arrayB):
    
    
    
    gcd_a = 0
    for a in arrayA:
        gcd_a = gcd(gcd_a, a)
    
                
    gcd_b = 0
    for b in arrayB:
        gcd_b = gcd(gcd_b, b)
    
    
    answer = [0]

    for b in arrayB:
        if(b%gcd_a==0):
            break         
    else:
        answer.append(gcd_a)

    for a in arrayA:
        if(a%gcd_b==0):
            break         
    else:
        answer.append(gcd_b)
        
        
    
    
    return max(answer)