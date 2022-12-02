from collections import deque

inp = input().strip()
boom = input().strip()
idx = 0

result = []
storage = deque()
for i in range(len(inp)):
    result.append(inp[i])

    if(inp[i] == boom[0]):
        if(len(boom) == 1):
            result.pop()
            continue
        if(idx != 0):
            storage.appendleft(idx)
            idx = 0
        idx += 1
        
    elif(inp[i] == boom[idx]):
        if(idx != len(boom) - 1):
            idx += 1
        else:
            idx = 0
            if(storage):
                idx = storage.popleft()
            for _ in range(len(boom)):
                result.pop()
    else:
        storage = deque()
        idx = 0
        

result = "".join(result)

if(result == ""):
    print("FRULA")
else:
    print(result)

# Replace 사용시 시간초과 발생, Replace는 앞에서부터 하나씩만 변경하는 방식?
# 따라서, stack을 이용하는데 두번째 시도에서는 slice를 이용하면 시간이 오래 걸려서
# stack을 두개 이용해, 하나는 boom에 포함된 string을 저장하는 stack, 다른 하나는 boom의 첫 문자열이 나오면 이전의 index와 stack을 저장해두는 stack.
# +) substring 저장

# pop()은 시간복잡도가 O(1).

# 방법 2) stack에 넣고, bomb의 마지막 글자와 stack의 마지막이 같으면, string을 비교해 stack에서 제거
# -> 앞에서, 뒤에서 접근하는 방식에 따라 코드 길이가 달라짐