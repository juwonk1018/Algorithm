import sys
input = sys.stdin.readline
number = int(input().strip())

minimum = 100000
def makeOne(n, k):
    global minimum

    if(minimum <= k):
        return
    
    if(n==1):
        if(minimum > k):
            minimum = k
        return k
    
    if(n%2==0):
        makeOne(int(n/2), k+1)
    if(n%3==0):
        makeOne(int(n/3), k+1)
    makeOne(int(n-1), k+1)

makeOne(number,0)
print(minimum)
