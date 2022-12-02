import sys
n = int(sys.stdin.readline())
timetable = []
for _ in range(n):
   timetable.append(list(map(int,sys.stdin.readline().split())))

timetable.sort(key=lambda x: (x[1], x[0]))

finish = 0
ans = 0
for i in range(len(timetable)):
    if(timetable[i][0] >= finish):
        finish = timetable[i][1]
        ans +=1
 
print(ans)


# 가장 먼저 끝나는 것을 선택하는 Greedy Algorithm