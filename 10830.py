import sys
input = sys.stdin.readline

n, b = map(int, input().split())

def matmul(matrix1, matrix2):

    new_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
            new_matrix[i][j] = new_matrix[i][j] % 1000
    return new_matrix


def square(matrix, b):

    if(b==1):
        return matrix
    elif(b==2):
        return matrix_square
    elif(b % 2 == 0):
        temp = square(matrix, b//2)
        return matmul(temp, temp)
    elif(b > 2 and b % 2 == 1):
        temp = square(matrix, b//2)
        return matmul(matmul(temp, temp), matrix)

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

matrix_square = matmul(matrix, matrix)

ans = square(matrix, b)


for i in range(n):
    ans[i] = list(map(lambda x: x%1000, ans[i]))
    print(*ans[i])


# matrix multiplcation에서 곱한 뒤 % 1000을 이용해 나머지를 넣어둬서 시간초과 해결
# 왜 1000으로 나눈 나머지를 넣어도 성립하는가?  