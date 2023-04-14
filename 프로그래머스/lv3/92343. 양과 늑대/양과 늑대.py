from collections import deque
def solution(info, edges):
    # search 후 (양 - 늑대)가 큰 값부터 찾기? => Greedy한 방법으로는 (양-늑대)가 같은 경우 우선순위 구분 X 
    # => Bruteforce
    
    def search(sheep, wolf): # 양과 늑대의 수를 가지고 트리 순회
        visited = [[] for _ in range(len(info))]
        visited[0] = [[sheep, wolf], [0]] # [[양, 늑대], [route]]
        queue = deque([0])
        while(queue):
            cur = queue.popleft()
            for c in child[cur]:
                s, w = visited[cur][0][0], visited[cur][0][1]
                if(info[c] >= 0): # 해당 지역에 양, 늑대가 사라지면 계산 X
                    s += 1-info[c]
                    w += info[c]
                if(s > w):
                    visited[c] = [[s, w], visited[cur][1] + [c]]
                    queue.append(c)
        return visited
    
    
    def saveSheep(sheep, wolf):
        nonlocal ans
        ans = max(ans, sheep)
        
        visited = search(sheep, wolf)
        for t in visited: # 양 - 늑대가 최대인 부분을 발견
            n_sheep = n_wolf = 0
            if(t): # 해당 지점에 도달할 수 있다면 방문 후 재귀
                ratio, route = t[0], t[1]
                diff = ratio[0] - ratio[1] # 추가된 양 - 추가된 늑대
                if(info[route[-1]] == 0 and route[-1] != 0 and diff > 0): #양에 도착하고, 양이 더 많은 경우 찾기         
                    
                    stack = []
                    for v in route: # 방문 처리
                        if(info[v] == 0):
                            n_sheep += 1
                            stack.append([v, 0])
                        elif(info[v] == 1):
                            n_wolf += 1
                            stack.append([v, 1])
                        info[v] = -1
                    if(n_sheep == 0): # 늑대보다 양이 많은 경우가 없으면 종료
                        return
                    else:
                        saveSheep(sheep + n_sheep, wolf + n_wolf)
                        if(n_wolf == 0):
                            break
                        while(stack):
                            pos, value = stack.pop()
                            info[pos] = value
                    
                    
                
    child = [[] for _ in range(len(info))]
    for p, c in edges:
        child[p].append(c)
    
    ans = 1
    saveSheep(0, 0)
    
    return ans