from math import log

def checkBinaryTree(binaryTree, length):
    # print(binaryTree, length)
    if(length == 1):
        return True
    
    if(binaryTree[length//2] == '1'):
        return checkBinaryTree(binaryTree[:length//2], length//2) and checkBinaryTree(binaryTree[length//2 + 1:], length//2)
    
    else:
        for num in binaryTree:
            if(num == '1'):
                return False
        return True


def solution(numbers):
    answer = []
    for number in numbers:
        num_to_bin = bin(number).split('b')[1]
        
        length = 2** (int(log(len(num_to_bin), 2)) +1) - 1 #binary로 나타낸 길이보다 큰 2^n - 1을 찾기
        
        binaryTree = '0' * (length - len(num_to_bin)) + num_to_bin
        if(checkBinaryTree(binaryTree, length)):
            answer.append(1)
        else:
            answer.append(0)
        
    
    return answer

# 111
# 0111010

# 010 1 010
# 0101010