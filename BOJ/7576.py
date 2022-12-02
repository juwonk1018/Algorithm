"""
deque(pop보다 popleft()가 시간이 빠름), set(중복된 것을 표기하기 좋음) 생각하고
dx,dy에 저장해서 더한 값이 0<=x<n and 0<=y<m에 오는 걸로 모두 표현가능
모든 익은 토마토의 주변을 게산하기에는 연산이 길어져서 deque를 이용해 토마토 범위 제한
"""

import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int, input().strip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().strip().split())))

count = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1]

deque = deque()

for i in range(n):
    for j in range(m):
        if(arr[i][j]==1):
            deque.append([i,j])

while(deque):
    count +=1
    for _ in range(len(deque)):
        i,j = deque.popleft()
        for k in range(4):
            x = i+dx[k]
            y = j+dy[k]
            if(0<=x<n and 0<=y<m and arr[x][y]==0):
                arr[x][y] = 1
                deque.append([x,y])

count -=1
for i in range(n):
    for j in range(m):
        if(arr[i][j] == 0):
            count = -1

print(count)
