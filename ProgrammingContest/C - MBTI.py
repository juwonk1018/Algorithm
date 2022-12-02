import sys
input = sys.stdin.readline
m,n = map(int, input().strip().split())

ans = 0
arr = []
for i in range(m):
    arr.append(input().strip())


dir = [[0,1],[1,0],[1,1],[-1,1],[1,-1],[-1,-1],[-1,0],[0,-1]]
for i in range(m):
    for j in range(n):
        for a,b in dir:
            if(0<= i+3*a and i+3*a <m and 0<= j+3*b and j+3*b <n):
                if(arr[i][j] == "I" or arr[i][j] == "E"):
                    if(arr[i+a][j+b] == "N" or arr[i+a][j+b] == "S"):
                        if(arr[i+2*a][j+2*b] == "F" or arr[i+2*a][j+2*b] == "T"):
                            if(arr[i+3*a][j+3*b] == "P" or arr[i+3*a][j+3*b] == "J"):
                                ans+=1
print(ans)
