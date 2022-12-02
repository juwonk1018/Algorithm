from collections import deque
import sys
input = sys.stdin.readline
r,c = map(int, input().split())

board = [input() for _ in range(r)]
dxdy = [[0,1],[1,0],[0,-1],[-1,0]]

alphabet = [0 for _ in range(27)]
alphabet[ord(board[0][0])-64] = 1

ans = 1
def dfs(y,x, num):
    global ans
    for dy, dx in dxdy:
        ny = y + dy
        nx = x + dx
        if(0 <= nx and nx < c and 0 <= ny and ny < r):
            chr = ord(board[ny][nx]) - 64
            if(alphabet[chr] == 0):
                alphabet[chr] = 1
                ans = max(ans, num+1)
                dfs(ny,nx, num+1)
                alphabet[chr] = 0


dfs(0,0,1)
print(ans)

#bfs 사용시 set과 add를 이용하면 시간 내에 풀 수 있음 [set에서 in은 O(1)여서]
#dfs 사용시 alphabet의 index를 이용하여 O(1) 시간에 지나온 알파벳인지 확인가능
