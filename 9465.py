import sys
input = sys.stdin.readline

case = int(input().strip())
for i in range(case):
    num = int(input().strip())
    arr = []
    ans = [[0,0]]
    for i in range(2):
        arr.append(list(map(int,input().strip().split())))


    ans[0][0], ans[0][1] = arr[0][0], arr[1][0]
    for i in range(0,num):
        if(i==1):
            ans.append([ans[0][1] + arr[0][i], ans[0][0] + arr[1][i]])
        elif(i>1):
            ans1 = max(ans[i-1][1] + arr[0][i], ans[i-2][0] + arr[0][i], ans[i-2][1] + arr[0][i])
            ans2 = max(ans[i-1][0] + arr[1][i], ans[i-2][0] + arr[1][i], ans[i-2][1] + arr[1][i])
            ans.append([ans1,ans2])

    print(max(ans[-1]))

