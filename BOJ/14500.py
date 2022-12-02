import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

tetromino = [[[0,1],[0,1],[0,1]], #1
             [[1,0],[1,0],[1,0]],
             
             [[0,1],[1,0],[0,-1]], #2

             [[1,0],[1,0],[0,1]], #3
             [[1,0],[1,0],[0,-1]],
             [[0,1],[1,-1],[1,0]],
             [[0,1],[1,0],[1,0]],

             [[0,1],[0,1],[1,-2]],
             [[0,1],[0,1],[1,0]],
             [[1,0],[0,1],[0,1]],
             [[1,0],[0,-1],[0,-1]],
             
             [[1,0],[0,1],[1,0]], #4
             [[1,0],[0,-1],[1,0]],
             [[0,1],[1,0],[0,1]],
             [[0,-1],[1,0],[0,-1]],

             [[0,1],[0,1],[1,-1]], #5
             [[-1,1],[1,0],[1,0]],
             [[1,-1],[0,1],[0,1]],
             [[1,0],[1,0],[-1,1]]]


ans = 0
for i in range(n):
    for j in range(m):
        for next in tetromino:
            result = num[i][j]
            tempY, tempX = i, j
            for nextY,nextX in next:
                tempY += nextY
                tempX += nextX
                if(tempY < 0 or tempY >= n or tempX < 0 or tempX >=m):
                    break
                result += num[tempY][tempX]
            ans = max(result, ans)
print(ans)

#DFS depth 3인 경우가 tetromino
#시간 단축도 생각해보기