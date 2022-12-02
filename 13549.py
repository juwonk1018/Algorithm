from collections import deque
n, k = map(int, input().split())

queue = deque()
queue.append([n,0])

minTime = [100000] * 400001

minTime[n] = 0
while(queue):
    cur, time = queue.popleft()
    if(cur>100000 + minTime[k] or time > minTime[k]):
        continue

    if(minTime[cur+1] > time+1):
        minTime[cur+1] = time+1
        queue.append([cur+1, time+1])
    if(minTime[cur-1] > time+1 and cur >= 1):
        minTime[cur-1] = time+1
        queue.append([cur-1, time+1])
    if(minTime[cur*2] > time):
        minTime[cur*2] = time
        queue.append([cur*2,time])

    
print(minTime[k])

#첫번째 FIX : minTime[k] 보다 time이 크면, 기록할 필요 없음
#두번째 FIX : 자기 자신으로 가는 최단 시간을 0으로 설정하지 않아, +1, -1을 거쳐 2로 기록됨.


"""
import sys
n,m=map(int, sys.stdin.readline().split())
l=[0]*100001
for i in range(n):
    l[i]=n-i
for j in range(n+1,m+1):
    if j%2==0:
        l[j]=min(l[j-1]+1,l[j//2])
    else:
        l[j]=min(l[j-1]+1,(l[(j+1)//2])+1)
print(l[m])

"""

#위의 식에서는 j%2 == 1일때, l[(j+1)//2]+1 값을 min으로 두는 이유는
#l[j-1]에서 l[j//2]의 값을 min으로 가져올 수 있으므로
#실질적으로 l[j] = min(l[(j+1)//2]+1, l[j//2]+1 ... ) 이 된다.