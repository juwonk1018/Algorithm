import sys
input = sys.stdin.readline

line_num = int(input())

for i in range(line_num):
    num = 0
    line = list(map(int,input().strip().split()))
    queue = list(map(int,input().strip().split()))
    pointer = line[1]

    while(queue):
        #print(pointer)
        #print(queue)
        if(queue[0] != max(queue)):
            queue.append(queue.pop(0))
            if(pointer):
                pointer-=1
            else:
                pointer = len(queue) - 1
        else:
            queue.pop(0)
            num+=1
            if(pointer==0):
                print(num)
                break
            pointer-=1

