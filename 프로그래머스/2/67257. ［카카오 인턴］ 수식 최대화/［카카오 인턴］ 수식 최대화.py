from itertools import permutations
from collections import deque

def solution(expression):
    n = len(expression)
    operator = ['-', '+', '*']
    s, number = [], ""
    
    for i in range(n):    
        if expression[i] in operator:
            s.append(number)
            s.append(expression[i])
            number = ""
        else:
            number += expression[i]
    s.append(number)
    
    answer = 0
    for operators in permutations(operator, 3):
        s_copy = deque(s.copy())
        for op in operators:
            newStack = deque()
            
            while(s_copy): # 스택 탐색
                cur = s_copy.popleft()
                if(cur == op): # 원하는 operator를 찾으면, stack의 맨 위에 값과 다음 값을 연산
                    result = str(eval(newStack.pop() + cur + s_copy.popleft()))
                    newStack.append(result)
                else:
                    newStack.append(cur)
            
            s_copy = newStack
            
        answer = max(answer, abs(int(s_copy[0])))
    
    return answer