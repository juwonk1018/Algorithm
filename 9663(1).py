n = int(input())
row = [0 for i in range(n)]

ans = 0
def promising(idx):
    for i in range(0, idx):
        if(abs(row[idx] - row[i]) == abs(idx - i) or row[i] == row[idx]):
            return False
        
    return True



def n_queens(idx):
    global ans

    if(idx == n):
        ans +=1
    else:
        for i in range(n):
            row[idx] = i
            if promising(idx):
                n_queens(idx+1)

n_queens(0)
print(ans)


"""
여러 방법을 사용하였지만, recursion을 이용해 푸는 방법, 백트래킹 문제 더 풀어봐야 될 듯
"""