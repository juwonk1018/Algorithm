import sys, math
input = sys.stdin.readline

wlan, need = input().strip().split()
wlan_list = []


for i in range(int(wlan)):
    wlan_list.append(int(input().strip()))



left = 1
right = max(wlan_list)

while(left <= right):
    total = 0
    mid = (left+right)//2
    for i in range(int(wlan)):
        total += wlan_list[i]//mid
    if(int(need) > total):
        right = mid - 1
    else:
        left = mid + 1

print(right)


#이분 탐색에서 만족하는 값의 최대값 찾기.
#데이터는 descending order로 정렬되어 만족하는 값 중 가장 오른쪽 값을 찾으면 maximum value
