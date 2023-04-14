ans = 0
def solution(info, edges):
    def DFS(sheep, wolf, cur, nextList):
        
        sheep += info[cur] ^1
        wolf += info[cur]
        if(sheep <= wolf):
            return
        
        global ans
        ans = max(sheep, ans)
        
        for n in nextList:
            DFS(sheep, wolf, n, (nextList | set(child[n])) - set([n]))
    
    child = [[] for _ in range(len(info))]
    for p, c in edges:
        child[p].append(c)
    
    DFS(0, 0, 0, set(child[0]))
    return ans