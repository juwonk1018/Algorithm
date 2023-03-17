# 큰 종이부터 채우는 것은 반례가 존재. (하트 모양으로 1이 나열될 때 = 4/2/2/1/1/1/1, 3/3/3/1)
# 백트래킹 => 100개의 셀을 다 살펴보는 것은 문제가 되지 않지만, 순회를 하는 과정에서
# arr[i][j] == 1을 만족한 후, return을 해서 재귀를 끝내지 않으면 i,j가 0인 상태에서 search도 하면서 길어진다.

# Line 57의 return 하나로 속도가 엄청 갈림

import sys
input = sys.stdin.readline

arr = []
for _ in range(10):
    arr.append(list(map(int, input().split())))
    
num = sum([sum(arr[i][:]) for i in range(10)])
ans = float("INF")
currentPaper = [0,5,5,5,5,5] #사용한종이의 개수

def checkPaper(i, j, length):
    temp = 0
    for a in range(length):
        temp += sum(arr[i+a][j:j+length])

    if(length ** 2 == temp):
        return True
    else:
        return False

def fillPaper(number, cnt): #현재 상태, 현재까지 사용한 색종이, 남은 1의 수
    global ans

    if(number == 0):
        ans = min(ans, cnt)
        return

    if(cnt >= ans):
        return

    if not sum(currentPaper):
        return

    for i in range(10):
        for j in range(10):
            if arr[i][j]:
                for k in range(5, 0, -1):
                    if(i+k <= 10 and j+k <= 10 and currentPaper[k]):
                        if(checkPaper(i,j,k)): # k 길이의 색종이를 넣을 수 있으면 넣기 
                            for r in range(i, i+k):
                                for c in range(j, j+k):
                                    arr[r][c] = 0
                            currentPaper[k] -= 1
                            fillPaper(number - k**2 , cnt + 1)
                            currentPaper[k] += 1 #복구

                            for r in range(i, i+k):
                                for c in range(j, j+k):
                                    arr[r][c] = 1
                return              
            
fillPaper(num, 0)
print(ans)