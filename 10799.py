import sys
input = sys.stdin.readline

string = input().strip()

num = 0
stack = []
for i in range (0,len(string)):
    if(string[i] == "("):
        stack.append(string[i])
    elif(string[i] == ")"):
        if(i > 0 and string[i-1] == "("):
            stack.pop()
            num += len(stack)
        else:
            num += 1
            stack.pop()

print(num)


