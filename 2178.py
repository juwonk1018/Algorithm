n, m = map(int, input().split())
arr = []
mX = [0, 0, 1, -1]
mY = [1, -1, 0, 0]
cur = [0,0]
count = 1

for _ in range(n):
    arr.append(list(map(int,input())))

visited = [cur]
next = [cur]
while(True):
    new_next = []
    for a in next:
        for i in range(4):
            nextX = a[1] + mX[i]
            nextY = a[0] + mY[i]
            if(0<= nextX and nextX < m and 0<= nextY and nextY < n):
                if((arr[nextY][nextX] == 1) and [nextY,nextX] not in visited and [nextY,nextX] not in new_next):
                    new_next.append([nextY,nextX])
                    visited.append([nextY,nextX])
        
    next = new_next
    count += 1
    if([n-1,m-1] in next):
            print(count)
            break

    

'''visited를 [n][m]이라는 배열로 표현하면 시간 줄음'''