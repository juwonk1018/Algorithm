from collections import deque

def solution(n, computers):
    
    visited = [False] * n
    
    def DFS(index):
        cur = deque([index])
        while(cur):
            idx = cur.popleft()
            visited[idx] = True
            for connection in connectionList[idx]:
                if(visited[connection] == 0):
                    cur.append(connection)
            
    
    connectionList = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(computers)):
            if(computers[i][j] and i != j):
                connectionList[i].append(j)

                
    answer = 0
    for i in range(n):
        if(visited[i] == 0):
            DFS(i)
            answer += 1
    
    return answer