import sys

input = sys.stdin.readline

string = list(input().strip())

num = 1
while(string):
    for number in str(num):
        if(string and string[0] == number):
            string.pop(0)

    num += 1

print(num-1)