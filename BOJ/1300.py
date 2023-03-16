# A[i][j] = i*j인데, 나온 값들을 차례대로 A[i*j] = 1과 같은 방식으로 기록할 수 있다면?

# 이분탐색이 이렇게 적용되는구나 싶은 문제

n = int(input())
k = int(input())

start = 1; end = k #k번째 수는 k보다 작거나 같다. 

ans = 0
while(start < end): # 자신보다 작은 수가 k개 이상인 곳을 찾기.
    mid = (start + end)//2

    lessNumber = 0
    for i in range(1, n+1):
        lessNumber += min(mid//i, n)
    
    if(lessNumber < k): # mid보다 작은 수가 k개에 미치지 못한다면
        start = mid + 1
    elif(lessNumber >= k): # k와 같거나 큰 값이 나온다면 end를 멈추기 
        end = mid

print(start)