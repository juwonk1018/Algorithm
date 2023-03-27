from collections import deque
def solution(A,B):
    A.sort()
    B.sort()
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[len(B) - 1 - i]
    return answer