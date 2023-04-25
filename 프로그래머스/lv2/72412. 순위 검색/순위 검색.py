def solution(info, query):
    
    def find(score, s):
        left, right = 0, len(score) - 1
        
        while(left <= right):
            mid = (left + right)//2
            if(score[mid] >= s):
                right = mid - 1
            else:
                left = mid + 1
        
        return len(score) - left
    
    score = [[] for _ in range(24)]
    selectList = [["cpp","java","python"], ["backend", "frontend"], ["junior", "senior"], ["chicken", "pizza"]]
    
    for information in info:
        num = 0
        cnt = 8
        infoList = list(information.split())
        for a, b in zip(infoList, selectList):
            num += b.index(a) * cnt
            cnt /= 2
        
        score[int(num)].append(int(infoList[-1]))
    
    for i in range(24):
        score[i].sort()
    
    answer = []
    # print(score)
    for q in query:
        total = 0
        q = list(q.split(" "))
        l, p, c, f, s = q[0], q[2], q[4], q[6], q[7]
        for i in range(24):
            if(score[i]):
                if((l == selectList[0][int(i//8)] or l == '-') and (p == selectList[1][int((i%8)//4)] or p == '-') and (c == selectList[2][int((i%4)//2)] or c == '-') and (f == selectList[3][int(i%2)] or f == '-')):
                    total += find(score[i], int(s))
                    # print(q, i, total)
                
        answer.append(total)
    
    return answer