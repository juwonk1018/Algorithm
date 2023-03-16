# segment tree의 연습, 최댓값 저장

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sys.setrecursionlimit(100000)

arr = []
maxTree = [-float("INF")] * (n*4)
minTree = [float("INF")] * (n*4)

def maxSegment(start, end, index):
    
    if(start == end):
        maxTree[index] = arr[start] #빼먹지 말기
        return arr[start]

    mid = (start + end) // 2
    maxTree[index] = max(maxSegment(start, mid, index * 2), maxSegment(mid + 1, end, index * 2 + 1))
    
    return maxTree[index]

def minSegment(start, end, index):
    
    if(start == end):
        minTree[index] = arr[start]
        return arr[start]

    mid = (start + end) // 2
    minTree[index] = min(minSegment(start, mid, index * 2), minSegment(mid + 1, end, index * 2 + 1))
    
    return minTree[index]

def searchSegment(tree, start, end, index, left, right, isMax):
    if(left > end or right < start):
        if(isMax):
            return -float("INF")
        else:
            return float("INF")
        
    mid = (start+end) // 2
    if(left <= start and end <= right):
        return tree[index]
    
    if(isMax):
        return max(searchSegment(tree, start, mid, index * 2, left, right, isMax), searchSegment(tree, mid + 1, end, index * 2 + 1, left, right, isMax))
    else:
        return min(searchSegment(tree, start, mid, index * 2, left, right, isMax), searchSegment(tree, mid + 1, end, index * 2 + 1, left, right, isMax))
    
for _ in range(n):
    arr.append(int(input()))

maxSegment(0, n-1, 1)
minSegment(0, n-1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(searchSegment(minTree, 0, n-1, 1, a-1, b-1, 0), searchSegment(maxTree, 0, n-1, 1, a-1, b-1, 1))