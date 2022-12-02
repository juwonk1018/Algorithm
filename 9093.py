import sys
input = sys.stdin.readline

line_num = int(input())
stack = []
for i in range(line_num):
    line = input().strip()
    print(line[::-1])
    for j in range(len(line)):
        if(line[j] == " "):
            while(len(stack)):
                print(stack.pop(), end='')
            print(" ", end= '')
        else:
            stack.append(line[j])
    while(len(stack)):
        print(stack.pop(), end='')
    print("")
