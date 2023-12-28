import sys
input = sys.stdin.readline

n, k = map(int, input().split())

medal = [[] for _ in range(n+1)]
for _ in range(n):
    lst = list(map(int, input().split()))
    cur = lst[0]
    medal[cur] = lst[1:]

k_medal = medal[k]

ans = 1

def compareMedal(firstMedal, secondMedal):
    fg, fs, fb = firstMedal
    sg, ss, sb = secondMedal

    if(fg > sg):
        return True
    elif(fg == sg):
        if(fs > ss):
            return True
        elif(fs == ss):
            if(fb > sb):
                return True

    return False
        

for i in range(1, n+1):
    ans += compareMedal(medal[k], medal[i])

print(ans)