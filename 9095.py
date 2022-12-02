import sys
input = sys.stdin.readline
num = int(input().strip())

def go(num):
    if(num ==1):
        return 1
    elif(num ==2):
        return 2
    elif(num ==3):
        return 4
    else:
        return go(num-1) + go(num-2) + go(num-3)


for i in range(num):
    temp = int(input().strip())
    print(go(temp))


"""
dp = [0,1,2,4]
for _ in range(4,14): dp.append(sum(dp[-3:]) 이라는 방법도 존재
