import sys
input = sys.stdin.readline

while(True):
    string = input().strip()
    if(string == '0'):
        break
    else:
        while(len(string) > 1 and string[0] == string[-1]):
            string = string[1:-1]
        if(len(string) <= 1):
            print("yes")
        else:
            print("no")
            
#while (x:=input())!='0':print('yes'if x==x[::-1] else 'no')로 가
