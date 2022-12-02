import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split())
ans = [[i] for i in range(1,n+1)]

cnt = 1
while(cnt != m): 
    new_arr = []
    for i in range(0,len(ans)):
        for j in range(1,n+1):
            if(j not in ans[i]):
                new_arr.append(ans[i] + [j])
    ans = new_arr
    
    cnt+=1
for i in (ans):
    #print(' '.join(map(str,i)))를 사용하면 간편
    for j in i:
        print(j, end=" ")
    print()
