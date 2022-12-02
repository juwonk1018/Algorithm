import sys
input = sys.stdin.readline

ans = [[0] * 10 for _ in range(10)]

row = [[0] * 10 for _ in range(10)]
col = [[0] * 10 for _ in range(10)]
box = [[0] * 10 for _ in range(10)]

for i in range(1, 10):
    line = input().strip()
    for j in range(1, 10):
        num = int(line[j-1])
        ans[i][j] = num
        row[i][num] = 1
        col[j][num] = 1
        box[3 * ((i-1)//3) + (j+2)//3][num] = 1

flag = False
def sudoku(r, c):
    global flag
    if flag:
        return

    if(c == 10):
        r += 1
        c = 1

    if(r == 10):
        flag = True
        for i in range(1,10):
            print(''.join(map(str, ans[i][1:])))
        return

    if(ans[r][c]):
        sudoku(r, c+1)
    
    else:
        for i in range(1,10):
            if(row[r][i] == 0 and col[c][i] == 0 and box[3 * ((r-1)//3) + (c+2)//3][i] == 0):
                row[r][i] = col[c][i] = box[3 * ((r-1)//3) + (c+2)//3][i] = 1
                ans[r][c] = i
                
                sudoku(r, c+1)

                row[r][i] = col[c][i] = box[3 * ((r-1)//3) + (c+2)//3][i] = 0
                ans[r][c] = 0
    
sudoku(1,1)

#전형적인 backtracking 문제. array index 0을 출력해서 계속 틀림.. ㅠㅠ