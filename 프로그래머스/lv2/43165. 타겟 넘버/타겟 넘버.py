from collections import defaultdict

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    for i in range(0, 2**n):
        bitmask = bin(i)[2:].zfill(n)
        total = 0
        for j in range(n):
            if(bitmask[n-1-j] == '1'): # +
                total += numbers[j]
            elif(bitmask[n-1-j] == '0'): # -
                total -= numbers[j]
        if(total == target):
            
            answer += 1
        
    return answer