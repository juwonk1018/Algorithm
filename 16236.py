from dis import findlinestarts


n = int(input())
field = []
sharkLevel = 2
sharkPos = [0,0]
eatenFish = 0
moveX = [1, -1, 0, 0]
moveY = [0, 0, 1, -1]

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if(temp[j] == 9):
            sharkPos[0] = i
            sharkPos[1] = j                
    field.append(temp)

prevPos = [sharkPos]
nextPos = []
nextTarget = []
visited = [sharkPos]
distance = 1
move = 0

while(True):
    findTarget = False
    for _ in range(n*n):
        nextPos = []
        for a in prevPos:
            for k in range(4):
                nextX = a[0] + moveX[k]
                nextY = a[1] + moveY[k]
                if(0 <= nextX and nextX < n and 0 <= nextY and nextY < n):
                    if([nextX, nextY] not in visited):
                        if(field[nextX][nextY] <= sharkLevel):
                            nextPos.append([nextX,nextY])
                            visited.append([nextX,nextY])
                        if(0 < field[nextX][nextY] and field[nextX][nextY] < sharkLevel):
                            nextTarget.append([nextX,nextY])
                        
        

        #print(nextPos, prevPos, nextTarget, distance)
        
        prevPos = nextPos

        if(nextPos == []):
            break

        if(nextTarget):
            findTarget = True
            nextShark = [n+1,n+1]
            for x in nextTarget:
                if(x[0] < nextShark[0]):
                    nextShark = x
                elif(x[0] == nextShark[0] and x[1] <= nextShark[1]):
                    nextShark = x
            
            field[sharkPos[0]][sharkPos[1]] = 0
            field[nextShark[0]][nextShark[1]] = 9
            sharkPos = nextShark
            prevPos = [nextShark]

            eatenFish += 1
            move += distance
            if(eatenFish == sharkLevel):
                sharkLevel +=1
                eatenFish = 0


            nextTarget = []
            nextPos = []
            visited = [sharkPos]
            distance = 1
            #print("SharkPos : {}, Level : {}, EatenFish : {}, Move : {}".format(sharkPos, sharkLevel, eatenFish, move))
            break
        
        
        if(not(nextTarget)):
            distance+=1

    if(not(findTarget)):
        break
    #print(move)
print(move)