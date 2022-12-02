import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, list(input().strip()))))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1
    pos = [[0,1],[1,0],[0,-1],[-1,0]]
    while(queue):
        cur = queue.popleft()
        if([cur[0],cur[1]] == [n-1,m-1]):
            return visited[cur[0]][cur[1]][cur[2]]
        for dx, dy in pos:
            ny = cur[0] + dy
            nx = cur[1] + dx
            if(0<= ny and ny < n and 0<= nx and nx < m):
                if(arr[ny][nx] == 0 and visited[ny][nx][cur[2]] == 0):
                    visited[ny][nx][cur[2]] = visited[cur[0]][cur[1]][cur[2]] + 1
                    queue.append([ny,nx,cur[2]])
                elif(arr[ny][nx] == 1 and cur[2] == 0):
                    visited[ny][nx][1] = visited[cur[0]][cur[1]][cur[2]] + 1
                    queue.append([ny,nx,cur[2]+1])
                    
    return -1

print(bfs())

#BFS로 풀긴 했지만, 뚫은 경우와 그렇지 않은 경우를 3-dimensional array에 저장해서 하는 경우로 해야 시간초과가 발생하지 않음
#벽이 존재하는 경우는 visited를 체크하지 않더라도, 이후에 벽이 없는 경우를 만났을 때 visited 여부를 체크하므로 하지 않아도 됨