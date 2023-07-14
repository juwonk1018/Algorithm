# 사다리를 타고 이동한 뒤, 뒤 번호에 사다리가 존재하면 뱀을 타고 뒤로 이동하는 경우 존재.

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * 2 + [float("INF")] * 99
snake_or_ladder = [0] * 101

for i in range(n):
    x, y = map(int, input().split())
    snake_or_ladder[x] = y
    
for i in range(m):
    u, v = map(int, input().split())
    snake_or_ladder[u] = v

cur = deque([[1, 0]])

while(cur):
    pos, count = cur.popleft()


    for i in range(1,7):

        nextPosition = pos + i
        if(nextPosition > 100):
            continue

        if(snake_or_ladder[pos+i] and dp[snake_or_ladder[pos+i]] > count + 1):
            dp[snake_or_ladder[pos+i]] = count + 1
            cur.append([snake_or_ladder[pos+i], count+1])

        elif(snake_or_ladder[pos+i] == 0 and dp[nextPosition] > count + 1):
            dp[nextPosition] = count + 1
            cur.append([nextPosition, count+1])


print(min(dp[100:]))