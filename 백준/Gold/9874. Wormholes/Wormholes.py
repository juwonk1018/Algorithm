import sys
input = sys.stdin.readline

def makePairs(cur, paired):

    global ans

    if(len(cur) == n//2): #짝이 모두 완성
        checkCycle(cur)
        return

    for i in range(n):
        if(i not in paired): # 짝이 지어지지 않으면, 짝을 만들고 중복을 제거하기 위해 break
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
        sx, sy = w
        
        while(True):
            
            for i in range(n):
                if(cy == wormholePosition[i][1] and wormholePosition[i][0] > cx):
                    cx = wormholePosition[i][0]
                    break
            else:
                break

            cx, cy = wormhole[(cx,cy)]

            if(cx == sx and cy == sy):
                ans += 1
                return

            
                    
        

n = int(input())

wormholePosition = []

for _ in range(n):
    x, y = map(int, input().split())
    wormholePosition.append((x,y))
    
wormholePosition.sort(key = lambda x : (x[1], x[0]))
ans = 0
makePairs([], [])

print(ans)