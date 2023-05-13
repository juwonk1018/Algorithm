from itertools import permutations
def isPrime(x):
    if(x < 2):
        return False
    
    for i in range(2, int(x**(1/2))+1):
        if(x % i == 0):
            return False
    return True

def solution(numbers):
    n = len(numbers)
    answer = set()
    for i in range(1,n+1):
        for arr in permutations(numbers, i):
            num = int(''.join(arr))
            answer.add(num)
            
    for num in [0,1] + list(answer):
        if(not(isPrime(num))):
            answer -= set([num])
            
    print(answer)
    return len(answer)