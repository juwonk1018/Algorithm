import sys
input = sys.stdin.readline
number = int(input().strip())

arr = {1:0, 2:1}


def makeOne(n):

    if(n in arr): return arr[n]
    arr[n] = min(makeOne(n//2)+n%2, makeOne(n//3)+n%3)+1
    return arr[n]
    

print(makeOne(number))


#array에 최소로 갈 수 있는 횟수를 기록해서(memoization) 이를 활용  
