import sys
input = sys.stdin.readline

n = int(input())

schedule = [[]]

for _ in range(n):
    t, p = map(int, input().split())
    schedule.append([t,p])

dp = [0] * (n+1)

answer = 0

def calc(i, cost):
    
    global answer
    answer = max(answer, cost)

    if(i > n):
        return

    t, p = schedule[i]
    
    if(i+t <= n+1):    
        calc(i+t, cost+p)
    calc(i+1, cost)

calc(1, 0)

print(answer)