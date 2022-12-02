import sys
input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    print("Material Management " + str(i+1))
    m = int(input().strip())
    ans = list(map(int, input().strip().split()))
    
    for j in range(m):
        sum = 0
        sum2 = 0
        temp = list(map(int, input().strip().split()))
        sum += temp[0]
        sum2 += temp[1]

    print("Classification ---- End!")
        
