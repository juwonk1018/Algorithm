import sys
input = sys.stdin.readline
M,N = map(int,input().strip().split())
arr = []
for i in range(M):
    arr.append(input().strip())


ans = 2500
for i in range(M-7):
    cur = arr[i:i+8]
    for j in range(N-7):
        white = 0
        black = 0
        temp = []
        for k in range(i,i+8):
            for l in range(j,j+8):
                if((k+l)%2 == 0):
                    if(arr[k][l] == "W"):
                        white+=1
                    elif(arr[k][l] == "B"):
                        black+=1
                elif((k+l)%2 == 1):
                    if(arr[k][l] == "B"):
                        white+=1
                    elif(arr[k][l] == "W"):
                        black+=1
        ans = min(ans,white,black)
print(ans)
        

    
