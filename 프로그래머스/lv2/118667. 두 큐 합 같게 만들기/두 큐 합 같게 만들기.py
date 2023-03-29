from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    s1, s2 = sum(queue1), sum(queue2)
    n = len(queue1) + len(queue2)
    
    while(answer <= n*2):
        if(s1 > s2):
            num = queue1.popleft()
            queue2.append(num)
            answer += 1
            s1 -= num
            s2 += num
        elif(s1 < s2):
            num = queue2.popleft()
            queue1.append(num)
            answer += 1
            s2 -= num
            s1 += num
        else:
            return answer

    return -1