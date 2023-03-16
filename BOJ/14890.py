import sys
input = sys.stdin.readline

n, l = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = 0

#가로 방향으로 체크
for i in range(n):
    canPass = True
    slope = [0] * n # 슬로프를 놓은 위치 확인
    for j in range(n-1):
        if(arr[i][j] > arr[i][j+1]): #높이가 작아질 경우
            for k in range(1,l+1):
                if(j+k < n):
                    slope[j+k] = 1 # 내려가려면 슬로프를 무조건 둬야되므로, 후에 해당 위치를 사용하려해도 여기서 False로 미리 처리됨
                    if(arr[i][j+k] != arr[i][j] - 1): # 작아지기 전 높이보다 모두 1 작지 않으면 불가능.
                        canPass = False
                else:
                    canPass = False
        elif(arr[i][j] < arr[i][j+1]):
            for k in range(1,l+1):
                if(j+1-k >= 0):
                    if(arr[i][j+1-k] != arr[i][j+1] - 1 or slope[j+1-k] == 1):
                        canPass = False
                else:
                    canPass = False
    if(canPass):
        ans +=1

#세로 방향으로 체크
for i in range(n):
    canPass = True
    slope = [0] * n # 슬로프를 놓은 위치 확인
    for j in range(n-1):
        if(arr[j][i] > arr[j+1][i]): #높이가 작아질 경우
            for k in range(1,l+1):
                if(j+k < n):
                    slope[j+k] = 1
                    if(arr[j+k][i] != arr[j][i] - 1): # 작아지기 전 높이보다 모두 1 작지 않으면 불가능.
                        canPass = False
                else:
                    canPass = False
        elif(arr[j][i] < arr[j+1][i]):
            for k in range(1,l+1):
                if(j+1-k >= 0):
                    if(arr[j+1-k][i] != arr[j+1][i] - 1 or slope[j+1-k] == 1):
                        canPass = False
                else:
                    canPass = False
    if(canPass):
        ans +=1
print(ans)