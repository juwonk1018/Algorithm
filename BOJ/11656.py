import sys
input = sys.stdin.readline
string = input().strip()
stack = []

for i in range(len(string)):
    stack.append(string[i:])

stack.sort()
for i in range(len(stack)):
    print(stack[i])
