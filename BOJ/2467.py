#two pointer 문제(다시 살펴보기)

# 0이나 양수나 음수에서만 나오는 경우 ( -5 2 2 ) 등의 edge case를 고려..
# -> 양 끝에서 줄어들게 하면 훨씬 쉬워짐..

n = int(input())
arr = list(map(int, input().split()))

minVal = float("INF")
idx = -1; ans = []; cnt = 0


for i in range(len(arr)):
    if(arr[i] > 0 and idx == -1): #양수 시작하는 위치 체크
        idx = i
    if(arr[i] == 0): #중성이 2개 이상인지 체크
        cnt += 1

if(len(arr[idx:]) >= 2):
    if(minVal > arr[idx] + arr[idx+1]):
        minVal = arr[idx] + arr[idx+1]
        ans = [arr[idx], arr[idx+1]]

if(len(arr[:idx]) >= 2):
    if(minVal > abs(arr[idx-1] + arr[idx-2])):
        minVal = abs(arr[idx-1] + arr[idx-2])
        ans = [arr[idx-2], arr[idx-1]]

if(idx == -1): #음수만 존재하는 경우
    ans = [arr[-2], arr[-1]]

elif(idx == 0): # 양수만 존재하는 경우
    ans = [arr[0], arr[1]]

else:
    sm = idx-1 #음수 시작하는 지점
    sp = idx #양수가 시작하는 지점
    while(True):
        if(sm < 0 or sp >= n):
            break

        if(abs(arr[sm] + arr[sp]) < minVal):
            minVal = abs(arr[sm] + arr[sp])
            ans = [arr[sm], arr[sp]]
            if(minVal == 0):
                break

        if(abs(arr[sm]) > abs(arr[sp])):
            sp +=1
        elif(abs(arr[sp]) > abs(arr[sm])):
            sm -=1
             
if(cnt >= 2):
    print(0, 0)
elif(cnt == 1):
    minVal = float("INF")
    minIdx = -1
    for i in range(n):
        if(arr[i] != 0 and abs(arr[i]) < minVal):
            minVal = abs(arr[i])
            minIdx = i
    
    if(minVal < sum(ans)):
        ans = [0, ans[minIdx]]
        ans.sort()
    
    print(ans[0], ans[1])
        
else:
    print(ans[0], ans[1])



#SOL 2 (간단한 버전)

n = int(input())
arr = list(map(int, input().split()))
ans = abs(arr[0] + arr[n-1])
ans_left = 0
ans_right = n-1

left_idx = 0; right_idx = n-1
while left_idx < right_idx:
    minVal = arr[left_idx] + arr[right_idx]

    if abs(minVal) < ans:
        ans_left = left_idx
        ans_right = right_idx
        ans = abs(minVal)

        if ans == 0:
            break
    if minVal < 0:
        left_idx +=1
    else:
        right_idx -= 1

print(arr[ans_left], arr[ans_right])

