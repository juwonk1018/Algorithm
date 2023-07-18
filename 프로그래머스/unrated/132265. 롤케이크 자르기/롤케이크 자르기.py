from collections import defaultdict

def solution(topping):
    
    toppingSet = defaultdict(int)
    curSpecies = defaultdict(int)
    
    for i in range(len(topping)):
        toppingSet[topping[i]] += 1
    
    
    answer = 0
    for i in range(len(topping)):
        if(topping[i] in toppingSet):
            toppingSet[topping[i]] -= 1
            if(toppingSet[topping[i]] == 0):
                del toppingSet[topping[i]]
        
        curSpecies[topping[i]] += 1
            
        if(len(curSpecies) == len(toppingSet)):
            answer += 1
            
    return answer