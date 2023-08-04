import heapq, sys
input = sys.stdin.readline

n = int(input())

room = []
for _ in range(n):
    room.append(list(map(int, list(input().split()[0]))))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


ans = [[-1] * n for i in range(n)]
ans[0][0] = 0

q = [[0, [0,0]]] # 방 변화 횟수

while(q):
    change, cur = heapq.heappop(q)
    
    if(change > ans[cur[0]][cur[1]]):
        continue

    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]

        if(0 <= nx < n and 0 <= ny < n and ans[nx][ny] == -1):
            if(room[nx][ny] == 1):
                heapq.heappush(q, [change, [nx,ny]])
                ans[nx][ny] = change
            elif(room[nx][ny] == 0):
                heapq.heappush(q, [change + 1, [nx,ny]])
                ans[nx][ny] = change + 1

print(ans[n-1][n-1])