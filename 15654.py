n, m = map(int, input().split())

original = list(map(int, input().split()))
original.sort()

stack = []
def bt():
    if(len(stack) == m):
        print(' '.join(map(str,stack)))
        return
    
    for i in original:
        if i not in stack:
            stack.append(i)
            bt()
            stack.pop()
bt()


"""
내 답안
ans = []
for i in range(n):
    ans.append([original[i]])

for _ in range(m-1):
    new_ans = []
    for element in ans:
        for i in original:
            new_arr = element.copy()
            if(i not in new_arr):
                new_arr.append(i)
                new_ans.append(new_arr)
    ans = new_ans

for element in ans:
    print(*element)
"""