def solution(key, lock):
    
    
    kx, ky = len(key), len(key[0])
    lx, ly = len(lock), len(lock[0])
    
    holeNumber = 0
    for i in range(lx):
        for j in range(ly):
            if(lock[i][j] == 0):
                holeNumber += 1
    
    keyPosition = []
    for i in range(kx):
        for j in range(ky):
            if(key[i][j] == 1):
                keyPosition.append([i,j])
    
    for _ in range(4):
        for i in range(len(keyPosition)):
            keyPosition[i][0], keyPosition[i][1] = keyPosition[i][1], kx - keyPosition[i][0]


        for i in range(-kx, lx):
            for j in range(-ky, ly):
                num = 0
                for ki, kj in keyPosition:
                    ni, nj = i + ki, j + kj
                    if(0 <= ni < lx and 0<= nj < ly):
                        if(lock[ni][nj] == 0):
                            num += 1
                        else:
                            break

                if(num == holeNumber):
                    return True

    return False