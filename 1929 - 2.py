import sys
input = sys.stdin.readline

start, end = input().strip().split()

arr = [1] * (int(end)+1)
arr[1] = 0
for j in range(2, int(int(end)**(1/2)) + 1):
    if(arr[j] == 1):
        k = 2
        while(j*k <= int(end)):
            arr[j*k] = 0
            k +=1

for i in range(int(start), int(end)+1):
    if(arr[i] == 1):
        print(i)
        
        
#소수를 구하기 위해서는 제곱근까지만 계산해도 되며, overhead가 큰 경우에는
#1부터 N까지의 수를 직접 나눠서 구하는 것이 아닌 '에라토스테네스의 체'를 이용해
#Time complexity를 줄임.
        
