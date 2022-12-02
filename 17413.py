import sys
input = sys.stdin.readline
string = input().strip()
stack = []
tag = True
for i in range(len(string)):
    if(('a' <= string[i] and string[i] <= 'z') or ('0' <= string[i] and string[i] <= '9')):
        if(tag):
            stack.append(string[i])
        else:
            print(string[i],end="")
    elif(('A' <= string[i] and string[i] <= 'Z') or ('0' <= string[i] and string[i] <= '9')):
        if(tag):
            stack.append(string[i])
        else:
            print(string[i],end="")
    elif('<' == string[i] or '>' == string[i]):
        tag = not(tag)
        if('<' == string[i]):
            while(stack):
                print(stack.pop(), end="")
        print(string[i],end="")
    elif(' ' == string[i]):
        if(tag):
            while(stack):
                print(stack.pop(), end="")
            print(string[i],end="")
        else:
            print(string[i],end="")
while(stack):
    print(stack.pop(), end="")            
            



