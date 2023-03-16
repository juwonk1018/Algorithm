# list를 copy하는 것은 100000 * 100000의 time complexity의 위험이 있기 때문에, 이중 리스트로 [시간, 횟수]를 저장하도록 해야 시간초과가 안남.

# 나중에 다시보기.
n, k = map(int, input().split())

# [시간, 횟수]
posCount = [[-1, 0] for _ in range(100001)]; posCount[n] = [0,1]

prevPos = [n]
while(posCount[k][1] == 0): #횟수가 0이 아닐때까지
    curPos = set([])
    for pos in prevPos:
        for i in [pos -1, pos +1, pos * 2]:
            if(0<= i <= 100000):
                if(posCount[i][0] == -1): #처음 도달했다면
                    posCount[i][1] += posCount[pos][1]
                    posCount[i][0] = posCount[pos][0] + 1
                    curPos.add(i) #처음 도달한 수만 새로운 경우로 추가
                elif(posCount[i][0] == posCount[pos][0] + 1): #처음 도달한 것은 아니지만 최단거리라면
                    posCount[i][1] += posCount[pos][1]
            
    prevPos = list(curPos)
    
print(posCount[k][0]) #시간
print(posCount[k][1]) #횟수
