def solution(s):
    
    stack = []
    for i in range(len(s)):
        if(stack and s[i] == ')' and stack[-1] == '('):
            stack.pop()
            continue
        stack.append(s[i])
        
    return stack == []