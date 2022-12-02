import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())

#Left, Root, Right
inOrder = list(map(int, input().split()))
#Left, Right, Root
postOrder = list(map(int, input().split()))

position = [0] * (n+1)

for i in range(n):
    position[inOrder[i]] = i

def recursion(inOrderS, inOrderE, postOrderS, postOrderE):
    
    if(inOrderS > inOrderE or postOrderS > postOrderE):
        return

    root = postOrder[postOrderE]
    print(root, end = " ")

    rootIdx = position[root]
    
    leftSize = rootIdx - inOrderS
    rightSize = inOrderE - rootIdx
    recursion(inOrderS, inOrderS + leftSize - 1, postOrderS, postOrderS + leftSize - 1)
    recursion(inOrderE - rightSize + 1, inOrderE, postOrderE - rightSize, postOrderE - 1)
    
    return

recursion(0,n-1,0,n-1)


#메모리 부족으로 slicing이 아닌 index를 이용하여 recursion
#후위 표기법에서 root를 찾아 inOrder에서 찾은 뒤, 이를 기준으로 left, right를 나누면
#후위 표기법에서도 inOrder의 root index 기준으로 left,right가 나뉘는 점을 생각

#또한, position 배열을 이용하여 index를 recursion마다 일일이 찾지 말고, list에 저장해서 시간초과를 막음
#setRecursionLimit?