def solution(numbers):
    s = []
    answer = [-1] * len(numbers)
    
    for idx, number in enumerate(numbers):
        while(s and s[-1][1] < number):
            curIdx, n = s.pop()
            answer[curIdx] = number
    
        s.append([idx,number])
    
    return answer