n = int(input())

n -= 1
i = 1
while(n > 0):
    n -= 6 * i
    i += 1

print(i)