import sys
input = sys.stdin.readline

start, end = map(int, input().strip().split())


for i in range(start, end + 1):
    if(i == 1):
        continue

    else:
        for j in range(2, int(i**(1/2))+1):
            if(i%j==0):
                break
        else:
            print(i)
            
        
        
#소수를 구하기 위해서는 제곱근까지만 계산해도 되며, overhead가 큰 경우에는
#1부터 N까지의 수를 직접 나눠서 구하는 것이 아닌 '에라토스테네스의 체'를 이용해
#Time complexity를 줄임.
        
