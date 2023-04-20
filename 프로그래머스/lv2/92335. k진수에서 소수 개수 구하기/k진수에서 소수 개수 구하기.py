def ten2k(n,k):
    s = ''
    while(n != 0):
        s = str(n % k) + s
        n = n // k
    return s

def isPrimeNumber(n):
    if(n == 1):
        return False
    if(n == 2 or n == 3):
        return True
    
    for i in range(2, int(n**(1/2)) + 1):
        if(n%i == 0):
            return False
    return True

def check(num):
    count = 0
    number = ''
    
    for i in range(len(num)):
        if(num[i] != '0'):
            number += num[i]
        else:
            if(number != ''):
                if(isPrimeNumber(int(number))):
                    count += 1
                number = ''
                
    if(number != '' and isPrimeNumber(int(number))): #number가 존재한다면 prime check
        count += 1
        
    return count
def solution(n, k):
    num = ten2k(n,k)
    return check(num)