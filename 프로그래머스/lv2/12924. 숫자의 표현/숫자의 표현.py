def solution(n):
    s = answer = 0
    f = 1
    for i in range(1, n+1):
        s += i
        while(s > n):
            s -= f
            f += 1

        if(s == n):
            answer += 1
            
    return answer