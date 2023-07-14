n, m = map(int, input().split())

arr = list(map(int, input().split()))


def permutation(cur, m, cnt):
    global answer

    if(cnt < m):
        for i in range(n):
            if(cur and arr[i] >= cur[-1]):
                permutation(cur + [arr[i]], m, cnt+1)
    
    else:
        answer.append(cur)

answer = []

for i in range(n):
    permutation([arr[i]], m, 1)

for i in sorted(list(set(map(tuple, answer)))):
    for j in i:
        print(j, end = ' ')
    print()
