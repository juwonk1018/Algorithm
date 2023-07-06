def solution(p):
    def correctString(s):
        
        result = ""
        
        leftParen = 0
        rightParen = 0
        
        if(s== ""):
            return ""
        
        for i in range(len(s)):
            if(s[i] == '('):
                leftParen += 1
            elif(s[i] == ')'):
                rightParen += 1
                
            if(leftParen == rightParen):
                u, v = s[:i+1], s[i+1:]
                break
        
        
        stack = []
        for i in range(len(u)):
            if(u[i] == '('):
                stack.append('(')
            elif(stack and u[i] == ')'):
                stack.pop()
        
        if(stack):
            result += "("
            result += correctString(v)
            result += ")"
            for char in u[1:len(u)-1]:
                if(char == '('):
                    result += ')'
                elif(char == ')'):
                    result += '('
            
        else:
            result += u + correctString(v)
        
        return result
        
    answer = correctString(p)
    return answer