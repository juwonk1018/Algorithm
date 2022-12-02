import sys
input = sys.stdin.readline

m,n = map(int,input().strip().split())

arr = [[] for _ in range(m+1)]
for i in range(n):
    a,b = map(int,input().strip().split())
    arr[a].append(b)
    arr[b].append(a)
        
elements = [i for i in range(1,m+1)] 

ans = 0

while(elements):
    cur = elements[0]
    stack = [cur]
    while(stack):
        node = stack.pop(0)
        if(node in elements):
            elements.remove(node)
            for i in arr[node]:
                if(i not in stack):
                    stack.append(i)
    ans +=1

print(ans)
        

#stack에 들어있는 node를 이용해서 arr[node]의 elements를 추가하는데 겹치는거는 제외해야 시간 감소
