import sys
input = sys.stdin.readline

line = int(input().strip())
for i in range(line):
    array = input().strip().split()
    size = int(array[0])
    total = 0
    for j in range(1,size):
        
        for k in range(j+1,size+1):
            a = int(array[j])
            b = int(array[k])
            if(a<b):
                temp = a
                a = b
                b = temp
            while(b!=0):
                n = a%b
                a = b
                b = n
            total += a
    print(total)
