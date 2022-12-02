input = input()
stack = []
for i in range(len(input)):
    if("A" <= input[i] and input[i] <= "Z"):
        print(input[i], end = "")
    else:
        if(stack == []):
            stack.append(input[i])
        else:
            if(input[i] == "+" or input[i] == "-"):
                while(stack != [] and stack[-1] != "("):
                    print(stack.pop(), end = "")
                stack.append(input[i])

            elif(input[i] == "*" or input[i] == "/"):
                while(stack != [] and (stack[-1] == "*" or stack[-1] == "/")):
                    print(stack.pop(), end = "")
                stack.append(input[i])

            elif(input[i] == "("):
                stack.append(input[i])
            elif(input[i] == ")"):
                while(stack[-1] != "("):
                    print(stack.pop(), end = "")
                stack.pop()

while(stack):
    print(stack.pop(), end = "")