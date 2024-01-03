import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

ans = []

for i in range(n-1, -1, -1): # 큰 사람부터 배치 (n, n-1, ..., 1)
    
    t = 0
    if(not(ans)):
        ans.append(i+1)
        continue

    for j in range(len(ans)): # 현재 배열을 탐색해, 개수가 일치하면 삽입(큰 수부터 배치하면 index마다 키가 큰 사람의 수가 달라짐)
        if(t == arr[i]):
            ans.insert(j, i+1)
            break

        if(ans[j] > i+1):
            t += 1
    
    else: # 끝에 도달하면 배열의 맨 뒤에 추가
        ans.append(i+1)

print(*ans)