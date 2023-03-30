def solution(data, col, row_begin, row_end):
    r, c = len(data), len(data[0])
    data.sort(key=lambda x : (x[col-1], -x[0]))
    S = []
    for i in range(r):
        temp = 0
        for j in range(c):
            temp += data[i][j] % (i+1)
        S.append(temp)
    
    answer = S[row_begin-1]
    for i in range(row_begin, row_end):
        answer = answer ^ S[i]
    
    return answer