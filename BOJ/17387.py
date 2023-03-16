# CCW를 이용하는 문제
# 네 점이 한 직선을 지나는 경우 등의 조건을 잘 알아두기

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(a1, b1, a2, b2, a3, b3):
    val = (a2-a1) * (b3-b1) - (a3-a1) * (b2-b1)
    if(val > 0):
        return 1
    elif(val == 0):
        return 0
    else:
        return -1

d123 = ccw(x1,y1,x2,y2,x3,y3)
d124 = ccw(x1,y1,x2,y2,x4,y4)
d341 = ccw(x3,y3,x4,y4,x1,y1)
d342 = ccw(x3,y3,x4,y4,x2,y2)

if(d123 * d124 <= 0 and d341 * d342 <= 0):
    if(d123 * d124 == 0 and d341 * d342 == 0): #일직선 상일 때
        if(max(x1,x2) >= min(x3,x4) and min(x1,x2) <= max(x3,x4) and max(y1,y2) >= min(y3,y4) and min(y1,y2) <= max(y3,y4)):
            print("1")
        else:
            print("0")
    else:
        print("1")
else:
    print("0")