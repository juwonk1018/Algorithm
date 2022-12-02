import sys
input = sys.stdin.readline

lstack = list(input().strip())
rstack = []

line_num = int(input())

for i in range(line_num):
    command = input().strip().split()
    if(command[0] == "L"):
        if(lstack):
            rstack.append(lstack.pop())
    elif(command[0] == "D"):
        if(rstack):
            lstack.append(rstack.pop())
    elif(command[0] == "B"):
        if(lstack):
            lstack.pop()
    elif(command[0] == "P"):
        lstack.append(command[1])


print(''.join(lstack + list(reversed(rstack))))

#Stack을 두개로 분리해서 시간복잡도를 최소화 시킴
