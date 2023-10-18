n = int(input())

arr = [0,1,2,3,4,5,6,7,8,9]

ans = [0,1,2,3,4,5,6,7,8,9]


while(arr):
    new_arr = []
    for i in arr:
        for j in range(10):
            if(i%10 > j):
                new_arr.append(i*10 + j)
                ans.append(i*10 + j)
    arr = new_arr

if(n < len(ans)):
    print(ans[n])
else:
    print(-1)