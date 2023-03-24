# 1번의 자식 노드들은 최소 몇번 만에 되는지를 파악하고, 그 값의 최대값이 target을 완성할 수 있는 최소 루트.

# 사전 순으로 적게 나열하려면, 자식의 최소 횟수가 최소 루트의 길이보다 작다면 계속 1씩을 줄여서 행동

def solution(edges, target):
    
    if(sum(target) == 0): # 모두 0이라면 접근을 할 수 없음
        return [-1]
    
    def blockStack(t):
        num = 1 # 시작 위치는 1    
        while(pointer[num] != -1):
            temp = pointer[num]
            pointer[num] = next_point[pointer[num]] 
            num = temp
        
        if(target[num-1] == 0): # 0이 나오면, 종료
            return False        
        
        
        count[num].append(t)
        if(canMake[num] == False):
            if(len(count[num]) <= target[num-1] <= len(count[num]) * 3):
                canMake[num] = True
            return True
        else: # True였다가 False로 바뀌면 불가능하다는 것을 의미
            if(not(len(count[num]) <= target[num-1] <= len(count[num]) * 3)):
                return False
            else:
                return True
    
    child = [[] for _ in range(len(target) + 1)]
    for edge in edges: # child 삽입
        p, c = edge
        child[p].append(c)
        
    pointer = [-1] * len(child)
    next_point = [-1] * len(child)
    
    for i in range(len(child)): # 작은 순서로 정렬
        child[i].sort()
        if(len(child[i])):
            pointer[i] = child[i][0]
        for j in range(len(child[i])):
            if(j != len(child[i])-1):
                next_point[child[i][j]] = child[i][j+1]
            else:
                next_point[child[i][j]] = child[i][0]
    
    
    count = [[] for _ in range(len(child))]
    canMake = [False] * len(child)
    for i in range(1, len(child)):
        if(target[i-1] == 0):
            canMake[i] = True
            
    currentTime = 1
    while(sum(canMake) != len(target)):
        if(blockStack(currentTime)):
            currentTime += 1
        else:
            return [-1]
        
    answer = [0] * currentTime
    for i in range(1, len(count)):
        if(count[i]):
            total = len(count[i])
            num3 = (target[i-1] - total) // 2
            num2 = (target[i-1] - total) % 2
            num1 = total - num3 - num2
            
            for order in count[i]:
                if(num1):
                    answer[order] = 1
                    num1 -= 1
                elif(num2):
                    answer[order] = 2
                    num2 -= 1
                else:
                    answer[order] = 3
                    num3 -= 1
    return answer[1:]

