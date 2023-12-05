import sys
input = sys.stdin.readline

p = int(input())

for i in range(p):
    line = list(map(int, input().split()))
    lineNumber = line[0]
    numberList = line[1:]

    sortedList = list(sorted(numberList))

    count = 0
    for idx, element in enumerate(numberList):
        for i in range(idx + 1, len(numberList)):
            if(numberList[i] < element):
                count += 1

    print(lineNumber, count)