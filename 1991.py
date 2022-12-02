import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None


tree = BST()

nodeArr = []
for i in range(65,91):
    nodeArr.append(Node(chr(i)))
for _ in range(n):
    root, left, right = input().split()
    if(left != "."):
        nodeArr[ord(root) - 65].left = nodeArr[ord(left) - 65]
    if(right != "."):
        nodeArr[ord(root) - 65].right = nodeArr[ord(right) - 65]

tree.root = nodeArr[0]

#PREORDER
queue = deque()
queue.append(tree.root)

preorder = ""
while(queue):
    cur = queue.popleft()
    preorder += cur.item
    if(cur.right != None):
        queue.appendleft(cur.right)
    if(cur.left != None):
        queue.appendleft(cur.left)
    

print(preorder)

#INORDER
queue = deque()
queue.append(tree.root)

inorder = ""
while(queue):
    cur = queue.popleft()
    if(cur.right != None):
        queue.appendleft(cur.right)
    queue.appendleft(cur)
    if(cur.left != None):
        queue.appendleft(cur.left)
    
    if(cur.left == None):
        cur = queue.popleft()
        inorder += cur.item
        while(cur.right == None and queue):
            cur = queue.popleft()
            inorder += cur.item
print(inorder)

#POST ORDER
queue = deque()
queue.append(tree.root)

postorder = ""
while(queue):

    cur = queue[0]
    if(cur.right != None):
        queue.appendleft(cur.right)
    if(cur.left != None):
        queue.appendleft(cur.left)
    
    if(cur.left == None and cur.right == None):
        cur = queue.popleft()
        postorder += cur.item
        while(queue and (queue[0].left == cur or queue[0].right == cur)):
            cur = queue.popleft()
            postorder += cur.item
print(postorder)


"""
recursion으로도 구현이 가능하지만, 위의 코드는 stack을 이용해 구현
"""