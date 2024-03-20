def solution(files):
    answer = []
    partedFile = []
    
    for idx in range(len(files)):
        file = files[idx]
        
        head, number, tail = "", "", ""
        startIdx, endIdx = -1, -1
        for i in range(len(file)):
            if(startIdx != -1 and not(file[i].isdigit())): # NUMBER가 아닌 부분이 나온다면 중단
                break
            if(file[i].isdigit()):
                if(startIdx == -1):
                    startIdx = i
                endIdx = i
                
        head = file[:startIdx]
        number = file[startIdx:endIdx+1]
        tail = file[endIdx+1:]
        partedFile.append([head, number, tail, idx])
                
    partedFile.sort(key=lambda x:[x[0].lower(),int(x[1]), idx])
    
    for h, n, t, idx in partedFile:
        answer.append(h+n+t)
    
    return answer