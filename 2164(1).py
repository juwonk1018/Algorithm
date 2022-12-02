"""deque의 popleft는 O(1)이지만, list의 pop(0)는 O(n)이라 느림."""
from collections import deque

import sys
input = sys.stdin.readline
n = int(input())
arr = deque(list(range(1,n+1)))

while(len(arr) !=1):
    arr.popleft()
    arr.append(arr.popleft())
print(arr[0])

"""(원하는 숫자 - (작은 숫자 중 가장 큰 2의 제곱)) * 2가 답"""
