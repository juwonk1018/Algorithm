from collections import deque
import heapq

def solution(board, skill):
    r, c = len(board), len(board[0])
    totalSumBoard = [[0] * (c+2) for _ in range(r+2)]
    
    for t, r1, c1, r2, c2, degree in skill:
        totalSumBoard[r1][c1] += (2*t - 3) * degree
        totalSumBoard[r1][c2+1] += -(2*t - 3) * degree
        totalSumBoard[r2+1][c1] += -(2*t - 3) * degree
        totalSumBoard[r2+1][c2+1] += (2*t - 3) * degree

    answer = 0
    for i in range(r):
        for j in range(c):
            if(j != 0):
                totalSumBoard[i][j] += totalSumBoard[i][j-1]
    
    for i in range(r):
        for j in range(c):
            if(i != 0):
                totalSumBoard[i][j] += totalSumBoard[i-1][j]
    
            if(board[i][j] + totalSumBoard[i][j] > 0):
                        answer += 1
                
        
    return answer