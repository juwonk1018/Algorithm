import sys
input = sys.stdin.readline

def makePairs(cur, paired):

    global ans

    if(len(cur) == n//2):
        checkCycle(cur)
        return

    for i in range(n):
        if(i not in paired):
            for j in range(i+1, n):
                if(j not in paired):
                    makePairs(cur + [[i, j]], paired + [i, j])
            break


def checkCycle(pairs):
    global ans

    wormhole = dict()
    
    for p1, p2 in pairs:
        wormhole[wormholePosition[p1]] = wormholePosition[p2]
        wormhole[wormholePosition[p2]] = wormholePosition[p1]

    for w in wormhole.keys():
        cx, cy = w
        cnt = 0
        
        while(True):
            cx, cy = wormhole[(cx,cy)]
            cnt += 1
            if(cnt >= 2 * n):
                ans += 1
                return

            nx = float("INF")
            for i in range(n):
                if(cy == wormholePosition[i][1] and wormholePosition[i][0] > cx):
                    nx = min(nx, wormholePosition[i][0])

            if(nx != float("INF")):
                cnt += 1
                if(cnt >= 2 * n):
                    ans += 1
                    return
                else:
                    cx = nx
                
            else:
                break
                    
        

n = int(input())

wormholePosition = []

for _ in range(n):
    x, y = map(int, input().split())
    wormholePosition.append((x,y))
    
ans = 0
makePairs([], [])

print(ans)