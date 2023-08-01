import sys
input = sys.stdin.readline


def getDivisor(num):
    divisorList = []

    for i in range(1, int(num**(1/2))+1):
        if(num % i == 0):
            divisorList.append(i)
            divisorList.append(num//i)
            
    return reversed(sorted(divisorList))

while(True):
    s = input().strip()

    if(s == '.'):
        break

    for l in getDivisor(len(s)):
        if(l * s[:len(s)//l] == s):
            print(l)
            break
        
        