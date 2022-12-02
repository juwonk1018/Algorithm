"""
int(bin(r)[2:],4)를 활용해 row의 경우는 위아래를 판별가능
'110'은 8를 기준으로 아래, 4를 기준으로 아래, 2을 기준으로 위
row는 아래의 것이 2배만큼 증가하고 column은 오른쪽 단순 덧셈
"""
import sys
input = sys.stdin.readline
ans = 0
n,r,c = map(int, input().strip().split())
while(n!=0):
    if(r >> (n-1)):
        ans += (2**n * 2**n)//2
        r -= 2**(n-1)

    if(c >> (n-1)):
        ans += (2**n * 2**n)//4
        c -= 2**(n-1)
    n -= 1
print(ans)
