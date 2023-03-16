# n은 5000이하인데, 메모리가 256MB이면 약 6700만 크기이므로 5000C2로 메모리 범위 안에 가능해진다.
# -> X, 하나를 고정해두고 two pointer를 사용하는 것인데, 처음과 끝에서 시작하는 것을 기억
# 함수로 풀면 더 빨리 풀림...
# -> global variable은 런타임에 추가되어 dict에 저장되므로 read/write에서 local variable보다 느림.

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

a1 = -1; a2 = -1; a3 = -1

def solve():
    minVal = float("INF")
    result = [-1, -1, -1]
    
    for i in range(n-2):
        start = i+1; end = n-1

        while(start < end):
            val = arr[i] + arr[start] + arr[end]
            if(abs(val) < abs(minVal)):
                result = [i, start, end]
                minVal = val
            
            if(val > 0):
                end -= 1
            elif(val < 0):
                start += 1
            elif(val == 0):
                break
    
    return result

ans = solve()
print(arr[ans[0]], arr[ans[1]], arr[ans[2]])
