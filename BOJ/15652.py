n, m = map(int, input().split())

ans = [[i] for i in range(1,n+1)]
for _ in range(m-1):
    new_ans = []
    for element in ans:
        for i in range(element[-1],n+1):
            new_arr = element.copy()
            new_arr.append(i)
            new_ans.append(new_arr)
    ans = new_ans

for element in ans:
    print(*element)
