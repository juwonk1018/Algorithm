# 11:50~

def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2+1):
        stack = []
        for j in range(0, len(s), step):
            if(stack and stack[-1][0] == s[j:j+step]):
                stack[-1][1] += 1
            else:
                stack.append([s[j:j+step], 1])
        length = 0
        for string, num in stack:
            if(num == 1):
                length += len(string)
            else:
                length += len(string) + len(str(num))
        answer = min(answer, length)
    
    return answer