import sys
input = sys.stdin.readline

num = int(input().strip())
ans = [[0,1]]
for i in range(1,num):
    ans.append([ans[i-1][0] + ans[i-1][1], ans[i-1][0]])

print(ans)
print(ans[-1][0]+ans[-1][1])
