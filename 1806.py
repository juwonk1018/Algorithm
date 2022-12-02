n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    arr[i] += arr[i-1]

p1 = 0
p2 = n
ans = 0

def index(step):
    global p1, p2
    for i in range(n+1-step):
        if(arr[i+step] - arr[i] >= s):
            p1 = i
            p2 = i + step
            return True

    return False

while(True):
    if(arr[p2] - arr[p1] >= s):
        ans = p2 - p1
        p2 -=1        
    else:
        if(not (index(p2-p1))):
            break

print(0 if arr[n] < s else ans)

# Two-pointer 문제

# 첫번째 시도 : arr의 각 index는 index까지의 합을 의미한다. 이를 통해, a부터 b(a<b) 까지의 부분합을 arr[b] - arr[a]를 통해 s와 비교함
# 두번째 시도 : 포인터를 두개 둬, 뒤에 있는 포인터를 조건을 충족시킬 때 줄여간다. 이후에 조건에 맞지 않는다면, 같은 길이의 부분합을 탐색해 포인터 두개 반환.
# - 0을 출력하는 경우는 수열의 모든 합이 s보다 작은 경우

# 정석 two-pointer는 array에 input을 그대로 저장해
# i,j라는 포인터가 존재하면 조건을 만족시키면 i를 증가시키고 s -= arr[i], ans = min(ans, j-i+1)
# 아니라면 j를 증가시켜서 s += arr[j]

# 즉, i부터 j까지의 부분합을 계속 갱신

"""
n, s = map(int, input().split())
arr = list(map(int, input().split()))

i = j = 0
total = arr[0]
ans = 100001

while(True):
    if(total >= s):
        ans = min(ans, j-i+1)
        total -= arr[i]
        i+=1
    else:
        if(j == n-1):
            break
        j+=1
        total += arr[j]

print(0 if ans == 100001 else ans)
"""