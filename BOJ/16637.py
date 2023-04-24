# 해결법을 구상하다가 시간이 많이 걸림.. 너무 복잡하게 생각한 문제가 아닌가 싶음


import sys
input = sys.stdin.readline

ans = 0
n = int(input())
expression = input().strip()


ans = -float("INF")
def calExpression(i, value):
    global ans

    if(i >= n-1):
        ans = max(ans, value)
        return
    # 앞을 먼저 계산
    nextValue = eval(str(value) + expression[i] + expression[i+1])
    calExpression(i+2, nextValue)

    # 뒤를 먼저 계산
    if(i < n-2):
        nextValue = eval(str(value) + expression[i] + str(eval(expression[i+1:i+4])))
        calExpression(i+4, nextValue)

calExpression(1, int(expression[0]))

print(ans)