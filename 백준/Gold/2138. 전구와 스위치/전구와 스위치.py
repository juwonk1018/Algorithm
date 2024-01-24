import sys

input = sys.stdin.readline

n = int(input())

ans = float("INF")
start = list(map(int, input().strip()))
target = list(map(int, input().strip()))

def toggleSwitch(arr, idx):

    if(idx > 0):
        arr[idx-1] = abs(1 - arr[idx-1])

    arr[idx] = abs(1 - arr[idx])

    if(idx < n-1):
        arr[idx+1] = abs(1 - arr[idx+1])


def switchStart(arr, cnt):
    global ans
    for i in range(1,n):
        if(arr[i-1] != target[i-1]):
            toggleSwitch(arr,i)
            cnt +=1
    
    if(arr == target):
        return cnt
    else:
        return -1

start_copy = start[:]
toggleSwitch(start_copy, 0)

c1, c2 = switchStart(start, 0), switchStart(start_copy, 1)

if(c1 != -1 and c2 != -1):
    print(min(c1,c2))

else:
    print(max(c1,c2))