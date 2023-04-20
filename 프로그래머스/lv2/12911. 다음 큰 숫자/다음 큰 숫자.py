def solution(n):
    answer = n+1
    cnt = bin(n)[2:].count('1')
    while(True):
        if(cnt == bin(answer)[2:].count('1')):
            return answer
        answer += 1