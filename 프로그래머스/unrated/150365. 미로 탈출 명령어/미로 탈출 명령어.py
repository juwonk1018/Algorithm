#BFS?

from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = 'z'*k
    
    queue = deque([[x,y,'']])
    
    visited = [[''] * (m+1) for _ in range(n+1)]
    
    dxdy = [[-1,0,'u'], [0,1,'r'], [0,-1,'l'], [1,0,'d']]
    while(queue):
        next_queue = []
        for dx, dy, alphabet in dxdy:
            for cur in queue:
                cx, cy, trace = cur
                
                trace_length = len(trace)
                if(trace_length >= k): # 다른 위치에 k 보다 많이 가거나, 절대적인 거리가 부족하다면
                    continue

                nx, ny, ntrace = cx + dx, cy + dy, trace + alphabet
                if(1 <= nx <= n and 1 <= ny <= m):
                    if(nx == r and ny == c and trace_length + 1 == k):
                        if(ntrace < answer):
                            answer = ntrace
                    else:
                        visited_length = len(visited[nx][ny])
                        if(visited[nx][ny] == ''):
                            visited[nx][ny] = ntrace
                            next_queue.append([nx, ny, ntrace])
                        elif(visited[nx][ny] != '' and trace_length + 1 > visited_length):
                            visited[nx][ny] = ntrace
                            next_queue.append([nx, ny, ntrace])
            
        queue = next_queue + []    
    answer = 'impossible' if answer == 'z' * k else answer
    return answer