maxScore = -float("INF")
answer = []

def solution(n, info):
    lionInfo = [0] * 11
    def select(num, idx):
        if(num < 0):
            return
        
        if(num == 0):
            global answer, maxScore
            apeachScore = 0
            lionScore = 0
            
            for i in range(11):
                if(info[i] and info[i] > lionInfo[i]):
                    apeachScore += 10-i
                elif(info[i] < lionInfo[i]):
                    lionScore += 10-i
            
            diff = lionScore-apeachScore
            
            if(diff > maxScore):
                maxScore = diff
                answer = lionInfo.copy()
            elif(diff == maxScore):
                if(lionInfo[::-1] > answer[::-1]):
                    answer = lionInfo.copy()
                        
            return 
        
        for i in range(idx, 11):
            if(lionInfo[i] == 0):
                arrow = info[i] + 1
                if(i == 10):
                    arrow = num
                lionInfo[i] += arrow
                select(num - arrow, i)
                lionInfo[i] -= arrow
        
    
    for i in range(11):
        if(lionInfo[i] == 0):
            arrow = info[i] + 1
            lionInfo[i] += arrow
            select(n - arrow, i)
            lionInfo[i] -= arrow
    
    if(maxScore <= 0):
        return [-1]
        
    return answer
    