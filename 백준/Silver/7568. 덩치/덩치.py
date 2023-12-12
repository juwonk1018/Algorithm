import sys
input = sys.stdin.readline

n = int(input())

person = []
for _ in range(n):
    x, y = map(int, input().split())
    person.append([x,y])

ans = []
for i in range(n):
    count = 1
    for j in range(n):
        if(person[i][0] < person[j][0] and person[i][1] < person[j][1]):
            count += 1
    ans.append(count)

print(*ans)