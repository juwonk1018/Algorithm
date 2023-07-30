from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

city = [list(map(int, input().split())) for _ in range(n)]

ans = float("INF")
dx = [0,-1,1,0]
dy = [1,0,0,-1]

def divideSection(x, y):
    
    global ans

    for d1 in range(1, n):
        for d2 in range(1, n):
            if(x+d1+d2 <= n-1 and 0 <= y-d1 < y < y+d2 <= n-1):
                sectionNumber = [[0] * n for i in range(n)]

                for i in range(d1+1):
                    sectionNumber[x+i][y-i] = 5
                for j in range(d2+1):
                    sectionNumber[x+d1+j][y-d1+j] = 5

                for i in range(d2+1):
                    sectionNumber[x+i][y+i] = 5
                for j in range(d1+1):
                    sectionNumber[x+d2+j][y+d2-j] = 5

                for i in range(x+d1): # Section 1
                    for j in range(y+1):
                        if(sectionNumber[i][j] == 5):
                            break
                        else:
                            sectionNumber[i][j] = 1

                for i in range(y+1, n): # Section 2
                    for j in range(x+d2+1): 
                        if(sectionNumber[j][i] == 5):
                            break
                        else:
                            sectionNumber[j][i] = 2

                for i in range(x+d1, n): # Section 3
                    for j in range(y-d1+d2):
                        if(sectionNumber[i][j] == 5):
                            break
                        else:
                            sectionNumber[i][j] = 3
                
                for i in range(x+d2+1, n): # Section 4
                    for j in range(n-1, y-d1+d2-1, -1):
                        if(sectionNumber[i][j] == 5):
                            break
                        else:
                            sectionNumber[i][j] = 4

                people = [0]*5
                for i in range(n):
                    for j in range(n):
                        if(sectionNumber[i][j] == 5):
                            people[0] += city[i][j]
                        else:
                            people[sectionNumber[i][j]] += city[i][j]
                
                if(ans > max(people) - min(people)):
                    ans = max(people) - min(people)

for x in range(n):
    for y in range(n):
        divideSection(x,y)

print(ans)