n, k = map(int, input().split())

fishBowl = list(map(int, input().split()))


for i in range(n):
    fishBowl[i] = [fishBowl[i]]


ans = 0
while(True):
    maxFish, minFish = max(list(map(max, fishBowl))), min(list(map(min, fishBowl)))

    if(maxFish - minFish <= k):
        print(ans)
        break

    # Step 1
    for i in range(len(fishBowl)):
        if(fishBowl[i][0] == minFish):
            fishBowl[i][0] += 1

    # print("Step 1 : ", fishBowl)
    # Step 2

    while(True):
        hoverBowl = [fishBowl[0][::-1]]; idx = 1
        while(fishBowl and idx < len(fishBowl) and len(fishBowl[idx]) >= 2):
            hoverBowl.append(fishBowl[idx][::-1])
            idx += 1

        hoverBowl = list(map(list, zip(*hoverBowl)))

        if(len(hoverBowl) > len(fishBowl) - idx):
            break
        else:
            for i in range(len(hoverBowl)):
                fishBowl[idx+i] = hoverBowl[i] + fishBowl[idx+i]
            fishBowl = fishBowl[idx:]

    # print("Step 2 : ", fishBowl)
    # Step 3

    dxdy = [[1,0], [-1,0], [0,1], [0,-1]]

    x = len(fishBowl)
    addFish = [[] + fishBowl[i] for i in range(x)]
    for i in range(x):
        fishBowl[i] = fishBowl[i][::-1]
        for j in range(len(fishBowl[i])):
            addFish[i][j] = 0
            
    for i in range(x):
        for j in range(len(fishBowl[i])):
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if(0<= nx < x and 0 <= ny < len(fishBowl[nx])):
                    if(fishBowl[i][j] - fishBowl[nx][ny] > 0):
                        addFish[nx][ny] += (fishBowl[i][j] - fishBowl[nx][ny])//5
                        addFish[i][j] -= (fishBowl[i][j] - fishBowl[nx][ny])//5

    for i in range(x):
        for j in range(len(fishBowl[i])):
            fishBowl[i][j] += addFish[i][j]


    for i in range(x):
        fishBowl[i] = fishBowl[i][::-1]


    # print("Step 3 : ", fishBowl)
    # Step 4
    fishBowl = [[fishBowl[i][j]] for i in range(len(fishBowl)) for j in range(len(fishBowl[i])-1, -1, -1)]

    # print("Step 4 : ", fishBowl)
    # Step 5
    for i in range(2):
        addBowl = []
        for i in range(len(fishBowl)//2-1, -1, -1):
            addBowl.append(fishBowl[i][::-1])

        for i in range(len(fishBowl)//2, len(fishBowl)):
            fishBowl[i] = addBowl[i-len(fishBowl)//2] + fishBowl[i]

        fishBowl = fishBowl[len(fishBowl)//2:]

    # print("Step 5 : ", fishBowl)
    # Step 6
    x, y = len(fishBowl), len(fishBowl[0])
            
    addFish = [[0] * y for _ in range(x)]

    for i in range(x):
        for j in range(len(fishBowl[i])):
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if(0<= nx < x and 0 <= ny < len(fishBowl[nx])):
                    if(fishBowl[i][j] - fishBowl[nx][ny] > 0):
                        addFish[nx][ny] += (fishBowl[i][j] - fishBowl[nx][ny])//5
                        addFish[i][j] -= (fishBowl[i][j] - fishBowl[nx][ny])//5

    for i in range(x):
        for j in range(len(fishBowl[i])):
            fishBowl[i][j] += addFish[i][j]

    # print("Step 6 : ", fishBowl)
    # Step 7
    fishBowl = [[fishBowl[i][j]] for i in range(len(fishBowl)) for j in range(len(fishBowl[i])-1, -1, -1)]
    # print("Step 7 : ", fishBowl)

    ans += 1
