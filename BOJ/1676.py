import sys
input = sys.stdin.readline

line = int(input().strip())
number = 0
number2 = 0
number5 = 0

if(line<2):
    number = 0

else:
    for i in range(1, line+1):
        while(True):
            if(int(i%2) == 0):
                i = i/2
                number2+=1
            elif(int(i%5) == 0):
                i = i/5
                number5+=1
            elif(i%10 == 0):
                i = i/10
                number+=1
            else:
                break

print(number + min(number2,number5))
