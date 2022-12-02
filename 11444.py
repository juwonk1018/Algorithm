n = int(input())

matrix = [[1,1],[1,0]]

def mul(A, B):
    n = len(A)
    newMatrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ans = 0
            for k in range(n):
                ans += A[i][k] * B[k][j]
            newMatrix[i][j] = ans % 1000000007
    return newMatrix

def power(matrix, p):
    if(p==1):
        return matrix
    else:
        temp =power(matrix, p//2)
        if(p%2 == 0):
            return mul(temp, temp)            
        else:
            return mul(mul(temp, temp), matrix)



print(power(matrix, n)[0][1])

#정답을 안보고는 풀지 못했을듯..? matrix multiplication의 거듭제곱을 이용해 수를 빠르게 줄일 수 있다.