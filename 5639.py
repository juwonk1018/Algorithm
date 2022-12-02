import sys
input = sys.stdin.readline

sys.setrecursionlimit(20000)


def postOrder(left, right):
    if(left == right):
        print(arr[left])
        return
    if(left > right):
        return

    for i in range(left+1, right+1):
        if(arr[i] > arr[left]):
            postOrder(left+1,i-1)
            postOrder(i,right)
            print(arr[left])
            break
        if(i == right):
            postOrder(left+1,right)
            print(arr[left])
    
arr = []

while True:
    try:
        cur = int(input())
        arr.append(cur)
    except:
        break

postOrder(0, len(arr)-1)


#idx의 부모보다 작으며 idx보다 큰 경우 : idx의 오른쪽 노드    
#idx의 부모보다도 크다면, root까지 idx를 바꾸며 더 큰 node를 찾음
#idx의 부모가 존재하지 않으면 idx(root)의 오른쪽 node(root의 경우)
        

#오른쪽에 추가하는 경우를 주의깊게 살펴보기

# TRY 1 : 오른쪽에 추가하는 경우에서, 부모 노드 중에서 자기보다 높은 값을 탐색 후 없으면 root를 기준으로 제일 오른쪽 값의 우측 노드로 설정(최대값)

# tree = [[-1,-1,-1] for _ in range(1000001)] #[root, left, right]
# root = int(input())
# idx = root
# 
# if(cur < idx):
#             tree[cur][0] = idx
#             tree[idx][1] = cur
#             idx = cur
#         if(cur > idx):
#             if(tree[idx][0] != -1 and tree[idx][0] < cur):
#                 while(tree[idx][0] < cur):
#                     idx = tree[idx][0]
#                     if(idx == root):
#                         break
#             while(tree[idx][2] != -1):
#                 idx = tree[idx][2]
#             tree[cur][0] = idx
#             tree[idx][2] = cur
#             idx = cur

# TRY 2 : 시간초과를 해결하기 위해서, input을 배열에 놓고 root, left, right를 root보다 큰 값을 찾을 시 분리


