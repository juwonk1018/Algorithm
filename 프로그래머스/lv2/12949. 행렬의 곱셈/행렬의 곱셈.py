def solution(arr1, arr2):
    x, y, z = len(arr1), len(arr2[0]), len(arr2)
    
    answer = [[0] * y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer