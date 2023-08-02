import sys

input = sys.stdin.readline

n = int(input())
maxBit = len(bin(100000)[2:])

seq = list(map(int, input().split()))
segmentBit = [0 for _ in range(4*n)] # segment tree
lazy = [0 for _ in range(4*n)]

def segment(start, end, idx):

    if(start==end):
        segmentBit[idx] = seq[start]
        return segmentBit[idx]

    mid = (start + end) // 2
    l_segment = segment(start, mid, idx * 2)
    r_segment = segment(mid+1, end, idx * 2 + 1)
    segmentBit[idx] = l_segment ^ r_segment

    return segmentBit[idx]

def update(start, end, idx, s, e, value): # value는 [0,1,0,1,0]과 같은 형태의 이진수 리스트
    
    if(lazy[idx]):
        segmentBit[idx] ^= (lazy[idx] * ((end - start + 1) %2))
        if(start != end):
            lazy[idx * 2] ^= lazy[idx]
            lazy[idx * 2 + 1] ^= lazy[idx]
        lazy[idx] = 0


    if(s > end or e < start):
        return segmentBit[idx]

    if(s<= start and end <= e):
        segmentBit[idx] = segmentBit[idx] ^ (value * ((end - start + 1) %2))
        if(start != end):
            lazy[idx * 2] ^= value
            lazy[idx * 2 + 1] ^= value
        return segmentBit[idx]
    
    mid = (start + end) //2

    l = update(start, mid, idx * 2, s, e, value)
    r = update(mid+1, end, idx * 2 + 1, s, e, value)
    segmentBit[idx] = l ^ r

    return segmentBit[idx]

    
def getSum(start, end, index, s, e):
    
    if(lazy[index]):
        segmentBit[index] ^= (lazy[index] * ((end - start + 1) %2))
        if(start != end):
            lazy[index * 2] ^= lazy[index]
            lazy[index * 2 + 1] ^= lazy[index]
        lazy[index] = 0
    
    if(end < s or start > e):
        return 0

    if(s <= start and end <= e):
        return segmentBit[index]
        
    
    mid = (start + end) //2

    l = getSum(start, mid, index * 2, s, e)
    r = getSum(mid + 1, end, index * 2 + 1, s, e)
    
    return l ^ r



segment(0, n-1, 1)

m = int(input())

for _ in range(m):
    query = list(map(int, input().split()))
    command = query[0]
    if(command == 1):
        i, j, k = query[1:]
        update(0, n-1, 1, i, j, k)

    elif(command == 2):
        i, j = query[1:]

        print(getSum(0, n-1, 1, i, j))  
