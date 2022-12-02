import sys
input = sys.stdin.readline

stack = [-1]*26

line = input().strip()
for i in range(len(line)):
    if(stack[ord(line[i])-97] == -1):
        stack[ord(line[i])-97] = i

for i in range(26):
    print(stack[i], end = ' ')
#ord로 char to int 변경
