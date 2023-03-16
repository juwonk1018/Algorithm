from collections import deque


import sys
input = sys.stdin.readline

dxdy = [[-1,0], [0,1], [1,0], [0,-1]]

m, n = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))
    
visited = [[0] * m for _ in range(n)]


cur = [[0,0]]

while(cur):
    cur.pop()