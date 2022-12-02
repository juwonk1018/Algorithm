channel = int(input())
num = int(input())
if(num != 0):
    work = set([i for i in range(0,10)]) - set(map(int, input().split()))
else:
    work = set([i for i in range(0,10)])


ans = 100; before = [""]; cur = []

for _ in range(min(len(str(channel))+1,6)):
    for element in before:
        for number in work:
            next = element + str(number)
            cur.append(next)
            if(abs(channel - int(next)) < abs(channel - ans)):
                ans = int(next)
            
    before = cur
    cur = []

print(min(len(str(ans))+abs(channel-ans), abs(100 - channel)))

#번호를 누르고 +,-로 이동 or [[100에서 직접 이동]] <- 이 경우를 생각해야함.  
#메모리가 많이 잡히긴하네..