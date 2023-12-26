import sys

t = int(input())

for _ in range(t):
    n, k, tid, m = map(int, input().split())

    submitNumber = [0] * (n+1)
    lastSubmit = [0] * (n+1)
    teamScore = [[0] * (k+1) for _ in range(n+1)]

    for i in range(m):
        cid, j, s = map(int, input().split())
        teamScore[cid][j] = max(teamScore[cid][j], s)
        lastSubmit[cid] = i
        submitNumber[cid] += 1


    ans = 1

    myTeamScore = sum(teamScore[tid])
    
    for i in range(1, n+1):
        if(i != tid):
            if(myTeamScore < sum(teamScore[i])):
                ans += 1

            elif(myTeamScore == sum(teamScore[i])):

                if(submitNumber[i] < submitNumber[tid]):
                    ans += 1

                elif(submitNumber[i] == submitNumber[tid]):

                    if(lastSubmit[i] < lastSubmit[tid]):
                        ans += 1
    
    print(ans)
            

