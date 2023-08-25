import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())

trucks = deque((map(int, input().split())))
bridge = [0] * w

ans = 0

while(True):

    if(not(trucks) and sum(bridge) == 0):
        break

    bridge = bridge[1:] + [0] # 트럭 한대를 보냄

    if(trucks and trucks[0] + sum(bridge) <= L): # 하중을 버틸 수 있으면 트럭 올림
        bridge[w-1] = trucks.popleft()

    ans += 1

print(ans)