import sys
input = sys.stdin.readline


west = 6
east = 2

wheel = [list(map(int, input().strip())) for _ in range(4)]

k = int(input())

def move(idx, direction):
    if(direction == 1):
        wheelCopy[idx] = [wheel[idx][7]] + wheel[idx][:7]
    elif(direction == -1):
        wheelCopy[idx] = wheel[idx][1:] + [wheel[idx][0]]
    

for _ in range(k):
    num, direction = map(int, input().split())

    num -= 1 # index를 [1-4]에서 [0-3]으로 조정

    wheelCopy = [wheel[i][:] for i in range(4)]

    for i in range(num-1, -1, -1):
        if(wheel[i][east] != wheel[i+1][west]):
            move(i, direction * (-1) ** (num-1-i+1))
            
        else:
            break

    for i in range(num+1, 4):
        if(wheel[i][west] != wheel[i-1][east]):
            move(i, direction * (-1) ** (i-num))
        else:
            break

    move(num, direction)

    wheel = [wheelCopy[i][:] for i in range(4)]

print(sum([wheel[i][0] * (2 ** i) for i in range(4)]))
