n = int(input())

for i in range(1, n+1):
    ans = 0
    lst = [0] * 26
    s = input().strip()
    f = input().strip()
    
    currentAlpha = []
    for alpha in f:
        lst[ord(alpha)-97] = 1
        currentAlpha.append(ord(alpha) - 97)

    for alpha in s:
        alphaIdx = ord(alpha) - 97
        minDist = float("INF")
        for selectedAlpha in currentAlpha:
            minDist = min(minDist, 26 - abs(alphaIdx - selectedAlpha), abs(alphaIdx - selectedAlpha))
        ans += minDist
    
    print("Case #"+str(i)+":",ans)