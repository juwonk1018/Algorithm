def solution(triangle):
    n =len(triangle[-1])
    answer = [0] * n
    
    for i in range(len(triangle)):
        currentAnswer = [0] * n
        for j in range(i+1):
            currentAnswer[j] = max(answer[max(j-1, 0)] + triangle[i][j], answer[j] + triangle[i][j])
            
        answer = currentAnswer + []
    return max(answer)