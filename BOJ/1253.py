# 2-pointer를 이용해, 다른 위치를 파악

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(n):
    s, e = 0, n-1

    while(s < e):
        if(arr[s] + arr[e] == arr[i]):
            if(s != i and e != i): # 다른 수라는 것을 확인
                ans += 1
                break
            else:
                if(s == i):
                    s+=1
                else:
                    e-=1

        elif(arr[s] + arr[e] > arr[i]):
            e -= 1
        else:
            s += 1

print(ans)