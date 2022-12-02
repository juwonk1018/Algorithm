import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())

def count2(n):
    num = 2
    count = 0
    while(num <= n):
        count += n//num
        num *= 2
    return count

def count5(n):
    num = 5
    count = 0
    while(num <= n):
        count += n//num
        num *= 5
    return count


print( min(count2(n) - count2(n-m) - count2(m), count5(n) - count5(n-m) - count5(m)))


# 30!의 경우에는 1*2*3...30인데, 30에서 2로 나누는 경우는 2의 배수를, 4로 나누는
# 경우에는 4 등 30보다 작은 2의 배수에 대한 2의 개수를 구할 수 있음.
