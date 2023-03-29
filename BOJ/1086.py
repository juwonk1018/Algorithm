# 15! 은 1300억개.. -> 앞에 온다는 것은 (어떤 수) * 10^n을 의미하므로
# 1. 같은 수라도 자리에 따라서 나머지가 달라짐
# 2. 다 더해도 결국은 자릿수가 똑같음
# 3. 해당 자릿수에 해당하는 dp..? bitmask..?

# 절반을 나눠서 나머지를 각자 구하고 합치기? => 사용 목록은 list? => 실패

# https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm < 유클리드 호제법 증명

from itertools import permutations
import sys, math

input = sys.stdin.readline


def gcd(a,b):
    if(b==0):
        return a
    return gcd(b, a%b)

n = int(input())


arr = list()
for _ in range(n):
    num = input().strip()
    arr.append(num)

k = int(input())

DP = [[0] * k for _ in range(2**n)] # [bitmask][0 ~ k-1] 

#remainder[n][k]는 나머지가 k 일때 n번째 index를 뒤에 두면 나머지 결과값
remainder = [[(i * (10 ** len(arr[j])) + int(arr[j])) % k for i in range(k)] for j in range(n)]
DP[0][0] = 1

for i in range(2**n): # i는 bitmask를 작은 것부터 접근
    for j in range(n): # 어떤 원소가 빠졌는지 확인
        if(i & (1<<j) == 0): #해당 index를 소유하지 않았다면
            for l in range(k): # 나머지를 순차적으로 탐색
                DP[i | (1<<j)][remainder[j][l]] += DP[i][l]

p = DP[2**n-1][0]
q = math.factorial(n)

g = gcd(p,q)

print(str(p//g)+'/'+str(q//g))