n, k = map(int, input().split())

conveyor = list(map(int, input().split()))
#conveyor = [conveyor[:n], conveyor[n:][::-1]]

robot = [0] * (2*n)

cnt = 0

ans = 1
while(True):
    # STEP 1
    
    conveyor = [conveyor[2*n-1]] + conveyor[0:2*n-1]
    robot = [robot[2*n-1]] + robot[0:2*n-1]


    if(robot[n-1] == 1):
        robot[n-1] = 0

    # STEP 2
    for i in range(n-1, -1, -1):
        nextPosition = i+1
        if(robot[i] == 1 and robot[nextPosition] == 0 and conveyor[nextPosition]):
            robot[nextPosition] = 1
            conveyor[nextPosition] -= 1
            robot[i] = 0

            if(conveyor[nextPosition] == 0):
                cnt += 1
    
    if(robot[n-1] == 1):
        robot[n-1] = 0

    # STEP 3
    if(conveyor[0]):
        conveyor[0] -= 1
        robot[0] = 1
        if(conveyor[0] == 0):
            cnt += 1


    # STEP 4
    if(cnt >= k):
        break

    ans += 1

print(ans)