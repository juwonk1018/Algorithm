def solution(s):
    stack = []
    for i in range(len(s)):
        if(stack and s[i] == stack[-1]):
            stack.pop()
            continue
        stack.append(s[i])
    return 0 if stack else 1