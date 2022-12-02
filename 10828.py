import sys
input = sys.stdin.readline

line = int(input())
stack = []
for i in range(line):
    
    line = input().strip()
    split_line = line.split(" ")
    if(split_line[0] == "push"):
        stack.append(split_line[1])
    elif(split_line[0] == "pop"):
        if(len(stack) >= 1):
            pop_element = stack.pop()
            print(pop_element)
        else:
            print("-1")
    elif(split_line[0] == "size"):
        print(len(stack))
    elif(split_line[0] == "empty"):
        if(len(stack) == 0):
            print("1")
        elif(len(stack) != 0):
            print("0")
    elif(split_line[0] == "top"):
        if(len(stack) <= 0):
            print("-1")
        else:
            print(stack[len(stack)-1])
        
            
    
