channel = int(input())
num = int(input())
if(num != 0):
    work = set([i for i in range(0,10)]) - set(map(int, input().split()))
else:
    work = set([i for i in range(0,10)])

ans = 100
before = [""]
cur = []

for _ in range(min(len(str(channel))+1,6)):
    for element in before:
        for number in work:
            next = element + str(number)
            cur.append(next)
            if(abs(channel - int(next)) < abs(channel - ans)):
                ans = int(next)
            
    before = cur
    cur = []

if(ans == 100):
    print(abs(channel - ans))
else: 
    print(min(len(str(ans))+abs(channel-ans), abs(100 - channel)))
