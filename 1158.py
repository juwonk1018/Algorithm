import sys
input = sys.stdin.readline

total, k = input().strip().split()
people = [1] * int(total)
current = -1

print("<", end='')
for i in range(int(total)):
    count = 0
    while(count < int(k)):
        current = (current + 1) % int(total)
        if(people[current] == 1):
            count = count + 1
    people[current] = 0
    print(current + 1, end = '')
    if(i != int(total) - 1):
        print(', ', end = '')

print(">")
