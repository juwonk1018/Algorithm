#정렬 후 two pointer?
# => count를 while 구문마다 쓰면 O(n^2)로 시간 초과 될 수 있어, 뒤에 몇개가 중복되는지 그 시점부터 세는 방식으로 변경
# PointerA > 0이 아닌 >= 0이라는 걸 주의

#defaultdict를 사용시 count가 더 편리
import sys
input = sys.stdin.readline

t = int(input())

# 부분합추가 후 정렬
n = int(input())
numA = list(map(int, input().split()))
partialSumA = []
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += numA[j]
        partialSumA.append(temp)    


partialSumA.sort()

m = int(input())
numB = list(map(int, input().split()))
partialSumB = []
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += numB[j]
        partialSumB.append(temp)    

partialSumB.sort()

pointerA, pointerB = len(partialSumA) - 1, 0
ans = 0
while(pointerA >= 0 and pointerB < len(partialSumB)):
    if(partialSumA[pointerA] + partialSumB[pointerB] == t):
        cnt = 1; cnt2 = 1
        while(pointerA != 0 and partialSumA[pointerA] == partialSumA[pointerA-1]):
            pointerA -= 1
            cnt += 1
        while(pointerB != len(partialSumB) - 1 and partialSumB[pointerB] == partialSumB[pointerB+1]):
            pointerB += 1
            cnt2 += 1
        pointerA -= 1
        pointerB += 1
        ans += cnt * cnt2
    elif(partialSumA[pointerA] + partialSumB[pointerB] < t):
        pointerB +=1
    else:
        pointerA -=1

print(ans)