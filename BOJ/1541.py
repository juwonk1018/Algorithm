""" -를 기준으로 split해서 첫번째 값의 합 - 나머지 값의 합을 하면 정답 """
import sys
import re
input = sys.stdin.readline
string = input().strip()
arr = []
op = [0]
for i in range(1, len(string)):
    if(string[i] == "+"):
       op.append(op[-1])
    elif(string[i] == "-"):
        op.append(op[-1] +1)
for cur in re.split('[+-]',string):
    arr.append(cur)


sum = 0
for i in range(len(arr)):
    if(i == 0):
        sum += int(arr[0])
    else:
        if(op[i] >0):
            sum -= int(arr[i])
        else:
            sum += int(arr[i])

print(sum)
