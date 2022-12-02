from collections import deque
n, k = map(int, input().split())

time = [0] * 100001
queue = deque()
queue.append(n)

while(queue):

    cur = queue.popleft()
    if(cur == k):
        print(time[k])
        break
    
    if(cur+1 <= 100000 and time[cur+1] == 0):
        queue.append(cur+1)
        time[cur+1] = time[cur] + 1
    if(cur-1 >= 0 and time[cur-1] == 0):
        queue.append(cur-1)
        time[cur-1] = time[cur] + 1
    if(cur*2 <= 100000 and time[cur*2] == 0):
        queue.append(cur*2)
        time[cur*2] = time[cur] + 1
