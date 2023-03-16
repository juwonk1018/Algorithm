# segment tree의 기본 : 구간 합

import sys
input = sys.stdin.readline


def segment(start, end, idx):
    if(start == end):
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start+end)//2
    tree[idx] = segment(start, mid, idx * 2) + segment(mid+1, end, idx * 2 + 1)

    return tree[idx]


def modify(start, end, index, pos, value): #arr[pos]의 값을 value로 변경하는 경우 segment tree 수정
    
    tree[index] += value
    if(start == end): 
        return
    
    if(start <= pos <= end):
        mid = (start+end)//2
        if(start <= pos <= mid):
            modify(start, mid, index * 2, pos, value)
        if(mid + 1 <= pos <= end):
            modify(mid + 1, end, index * 2 + 1, pos, value)

def intervalSum(start, end, index, left, right): #left, right는 구하고자 하는 범위
    if(end < left or right < start):
        return 0

    if(left <= start and end <= right):
        return tree[index]    
    mid = (start + end) // 2
    return intervalSum(start, mid, index * 2, left, right) + intervalSum(mid + 1, end, index*2 + 1, left, right)



n, m, k = map(int, input().split())
arr = []
tree = [0] * (n*4)
for _ in range(n):
    arr.append(int(input()))

segment(0, n-1, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    
    if(a==1):
        num = c - arr[b-1] #기존의 값을 빼고 새 값을 더하기
        modify(0, n-1, 1, b-1, num)
        arr[b-1] = c
    elif(a==2):
        print(intervalSum(0, n-1, 1, b-1, c-1))
