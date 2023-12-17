import sys
input = sys.stdin.readline

n, newScore, p = map(int, input().split())

if(n == 0):
    scoreList = []
    print(1)
else:
    scoreList = list(map(int, input().split()))
    scoreList = scoreList[:p]


    if(len(scoreList) == p):
        if(scoreList[-1] < newScore):
            cnt = 1
            for i in range(n):
                if(scoreList[i] > newScore):
                    cnt += 1
            print(cnt)
        else:
            print(-1)

    
    if(len(scoreList) != p): # 랭킹 등록 가능
        cnt = 1
        for i in range(n):
            if(scoreList[i] > newScore):
                cnt += 1 
        print(cnt)
