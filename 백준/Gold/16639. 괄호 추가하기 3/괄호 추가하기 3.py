import sys
input = sys.stdin.readline

def splitExpression(expression):
    if(expression.count("+") + expression.count("*") + expression.count("-") <= 1):
        return [eval(expression), eval(expression)] # 최대, 최소

    ans = [-float("INF"), float("INF")]
    for i in range(len(expression)):
        if(expression[i] == "+"):
            left, right = splitExpression(expression[:i]), splitExpression(expression[i+1:])
            ans[0] = max(ans[0], left[0] + right[0])
            ans[1] = min(ans[1], left[1] + right[1])
            
        if(expression[i] == "*"):
            left, right = splitExpression(expression[:i]), splitExpression(expression[i+1:])
            ans[0] = max(ans[0], left[0] * right[0], left[0] * right[1], left[1] * right[0], left[1] * right[1])
            ans[1] = min(ans[1], left[0] * right[0], left[0] * right[1], left[1] * right[0], left[1] * right[1])
        if(expression[i] == "-"):
            left, right = splitExpression(expression[:i]), splitExpression(expression[i+1:])
            ans[0] = max(ans[0], left[0] - right[1])
            ans[1] = min(ans[1], left[1] - right[0])
            
    return ans

n = int(input())
expression = input().strip()

print(splitExpression(expression)[0])
