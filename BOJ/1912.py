import sys
input = sys.stdin.readline

num = int(input().strip())

arr = list(map(int, input().strip().split()))
arr2 = [-1000] * num
for i in range(0, num):
    if(arr2[i] < arr[i]):
        arr2[i] = arr[i]
    if(i>0):
        total = arr2[i-1] + arr[i]
        if(total > arr2[i]):
            arr2[i] = total

    

print(max(arr2))


# for i in range(1,num): arr[i] = max(0,arr[i-1]) + arr[i]로 한줄로 표현 가능
