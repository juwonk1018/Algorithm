# bitmask? => 2^40
# 배열을 정렬 시, 음수, 0, 양수가 나오는데 arr안의 원소를 s만큼 뺴서 0을 만드는 경우로 변경?
# => 음수나 양수로 많이 몰린다면 시간이 많이걸림. 절반으로 나눈다.
# => 절반으로 나누면 2^20 = 1,048,576밖에 안나옴(이 부분을 생각못함)

from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = arr[:(n//2)]
right = arr[(n//2):]



ans = 0

leftSum = []
for i in range(1, len(left)+1):
    for element in list(combinations(left, i)):
        num = sum(element)
        leftSum.append(num)
        if(num == s):
            ans +=1

rightSum = [0] * 8000001
for i in range(1, len(right)+1):
    for element in list(combinations(right, i)):
        num = sum(element)
        rightSum[num] += 1
        if(num == s):
            ans +=1

leftSum.sort()

for num in leftSum:
    ans += rightSum[s - num]

print(ans)