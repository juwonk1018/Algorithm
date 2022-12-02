import sys
input = sys.stdin.readline

stack = [0]*26

line = input().strip()
for i in range(len(line)):
    stack[ord(line[i])-97] += 1

for i in range(26):
    print(stack[i], end = ' ')
#ord로 char to int 변경
