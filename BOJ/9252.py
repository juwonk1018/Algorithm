import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

len_a = len(a)
len_b = len(b)

dp = [[0, ""] for _ in range(len_b)]

for i in range(len_a):
    cur = 0 
    word = ""
    for j in range(len_b):
        if(dp[j][0] > cur):
            cur = dp[j][0]
            word = dp[j][1]

        else:
            if(a[i] == b[j]):
                dp[j][0] = cur + 1
                dp[j][1] = word + a[i]

print(dp)
print(*max(dp), sep = "\n")