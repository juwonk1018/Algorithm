import sys
input = sys.stdin.readline

line_num = int(input())

red = []
blue = []
green = []

for i in range(line_num):
    line = input().strip().split()

    if(i==0):
        red.append(int(line[0]))
        blue.append(int(line[1]))
        green.append(int(line[2]))

    else:
        red.append(min(blue[i-1] + int(line[0]),green[i-1] + int(line[0])))
        blue.append(min(red[i-1] + int(line[1]),green[i-1] + int(line[1])))
        green.append(min(red[i-1] + int(line[2]),blue[i-1] + int(line[2])))

print(min(red[line_num-1],blue[line_num-1],green[line_num-1]))
