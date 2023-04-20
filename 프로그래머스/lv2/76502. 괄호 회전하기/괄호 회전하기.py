def solution(s):
    
    answer = 0
    for i in range(len(s)):
        string = s[i:] + s[:i]
        result = 1; stack = []
        for a in string:
            if(a in ["[", "(", "{"]):
                stack.append(a)
            else:
                if(stack):
                    if(a == "]" and stack[-1] == "["):
                        stack.pop()
                    elif(a == ")" and stack[-1] == "("):
                        stack.pop()
                    elif(a == "}" and stack[-1] == "{"):
                        stack.pop()
                else:
                    result = 0
        if(stack):
            result = 0

        answer += result
    return answer