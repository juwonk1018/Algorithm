import sys
input = sys.stdin.readline

line = int(input().strip())

queue = []
for i in range(line):
    command = input().strip().split()
    if(command[0] == "push"):
        queue.append(command[1])
    elif(command[0] == "size"):
        print(len(queue))
    elif(command[0] == "pop"):
        if(len(queue)):
            print(queue[0])
            queue = queue[1:]
        else:
            print(-1)
    elif(command[0] == "empty"):
        print(0 if len(queue)>0 else 1)
    elif(command[0] == "front"):
        print(queue[0] if len(queue)>0 else -1)
    elif(command[0] == "back"):
        print(queue[len(queue)-1] if len(queue)>0 else -1)
