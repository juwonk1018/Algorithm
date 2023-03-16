# DP, bitmasking이 혼합된 문제

# n = 10(1) : 9876543210
# n = 11(3) : 98765432101, 89876543210, 10123456789
# n = 12(14) : 989876543210, 987876543210, 987656543210, ... , 987654321210
#        : 987654321010# , 898765432101, 789876543210,  987654321012, 210123456789, 101234567898,

# 계단 수에서 0-9가 모두 나타나는 경우 : 9876543210, 0123456789
# 계단 수에서 앞이 8일 때, 7,9를 붙여 길이를 늘리는 방식은 시간이 많이 걸린다.
# => 실제 수를 이용하지 않고, 앞과 뒤에 수가 몇개 있는지를 이용.

# => 연속으로 등장하는 것이 아닌 한번이라도 등장하는 조건이므로 위는 적용할 수 없음. (문제 이해를 잘못함)


# => 9876543210 등에서 이어 붙인다면 경우의 수가 복잡해지므로 DP와 bitmasking으로 푸는 방법

# 1 2 3 4 5 6 7 8 9로 처음에 시작하여 12 / 21, 23/ 32, 34 / ... 등으로 나아가면 겹치는 값이 없고 비트마스킹으로 계속 체크
# 1 << num으로 왼쪽부터 9876543210의 개수를 나타냄 | (or) 연산을 통해 나타냄

# !! 1024의 크기가 아닌 4의 크기로 두어, 0에 도달, 9에 도달의 조건을 bitmask로 00, 10, 01, 11로 나타내면 더 빠르게 연산가능

n = int(input())



next = [[1], [0,2], [1,3], [2,4], [3,5], [4,6], [5,7], [6,8], [7,9], [8]]

cur = [[0] * 1024 for _ in range(10)] # cur은 [10][1024] 크기의 배열이고, [i][j]는 i로 끝나는 수에서 j를 2비트로 변환해 0-9까지 어느 수가 들어있는지 check

for i in range(1, 10):
    cur[i][1<<i] = 1

ans = 0

for _ in range(n-1):
    cur_copy = [[0] * 1024 for _ in range(10)]
    for i in range(10): # 지난 cycle에서 i로 끝나며 0-9까지 수 중 어느 숫자가 나왔는지를 j를 통해 알아냄
        for j in range(1024):
            for num in next[i]:
                if(cur[i][j] != 0):
                    cur_copy[num][j | (1 << num)] += cur[i][j]

    cur = cur_copy.copy()
    
    
for i in range(10):
    ans += cur[i][1023]
print(ans % 1000000000)