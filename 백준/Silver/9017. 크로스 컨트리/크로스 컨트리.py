import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    team = [[] for _ in range(max(arr) + 1)]
    notCount = []

    for i in range(n):
        team[arr[i]].append(i)

    for i in range(1, max(arr)+1):
        if(len(team[i]) != 6):
            notCount.append(i)

    team = [[] for _ in range(max(arr) + 1)]
    
    count = 1
    for i in range(n):
        if(arr[i] not in notCount):
            team[arr[i]].append(count)
            count +=1

    ans = -1
    score = [float("INF"), float("INF")]
    for i in range(1, max(arr)+1):
        if(i not in notCount):
            sumScore = sum(team[i][:4])
            if(sumScore < score[0] or (sumScore == score[0] and team[i][4] < score[1])):
                score = [sumScore, team[i][4]]
                ans = i

    print(ans)