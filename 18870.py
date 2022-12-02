import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,(input().strip().split())))

temp = -10000000001
cnt = 0
new_arr = dict()
for i in sorted(arr):
    if(i > temp):
        new_arr[i] = cnt
        temp = i
        cnt+=1

for i in arr:
    print(new_arr[i],end =" ")'''


#set을 이용하면 중복을 제거할 수 있음
