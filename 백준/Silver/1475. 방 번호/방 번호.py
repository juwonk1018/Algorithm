n = input()

numberSet = [0] * 10

for i in range(len(n)):
    if(n[i] == '6' or n[i] == '9'):
        if(numberSet[6] < numberSet[9]):
            numberSet[6] += 1
        else:
            numberSet[9] += 1
    else:
        numberSet[int(n[i])] += 1

print(max(numberSet))