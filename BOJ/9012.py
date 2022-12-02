for i in range(int(input())):
    result = 0
    stack = []
    line = input()
    for j in range(len(line)):
        
        if(line[j] == "("):
            stack.append("(")
        elif(line[j] == ")"):
            if(len(stack) > 0):
                if(stack[-1] == "("):
                    stack.pop()
            else:
                result = 1
                break
    
    if(len(stack) or result):
        print("NO")
    elif(len(stack) == 0):
        print("YES")
    
