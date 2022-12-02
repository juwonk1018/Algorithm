import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split())
arr = [[] for i in range(n)]
checked = False

for _ in range(m):
    a1, a2 = map(int,input().strip().split())
    arr[a1].append(a2)
    arr[a2].append(a1)

def dfs(cur, visited):
    global checked
       
    for j in arr[cur]:
        visit = visited + []
        if(j not in visit):
            visit.append(j)
            if(len(visit) == 5):
                checked = True
                break
            if(not checked):
                dfs(j, visit)

for i in range(n):
    dfs(i, [i])

print("1" if(checked) else "0")


# visited가 아닌 array를 따로 만들어, dfs에 들어가면 checked, 나오면 check가 해제되는 방식도 생
