def solution(msg):
    n = len(msg)
    
    dictionary = dict()
    index = 27
    for i in range(1, 27): # 사전 초기화
        dictionary[chr(64+i)] = i
    
    curIndex = 0
    answer = []
    while(curIndex < n):
        lastIndex = -1
        for j in range(curIndex, n): # 가장 긴 문자열 w 찾기
            if(msg[curIndex:j+1] in dictionary):
                lastIndex = j
            else:
                break

        answer.append(dictionary[msg[curIndex:lastIndex+1]])

        if(lastIndex < n-1): # 다음 글자가 남아있다면, 사전 등록
            dictionary[msg[curIndex:lastIndex+1] + msg[lastIndex + 1]] = index
            index += 1
            
        curIndex = lastIndex + 1 # 다음 글자 업데이트
    
    
    return answer