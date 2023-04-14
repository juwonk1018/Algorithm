def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    answer = [0, 0]
    rank = [6,6,5,4,3,2,1]
    while(lottos):
        cur = lottos.pop() 
        if(cur==0):
            answer[1] += 1
            continue
        
        while(win_nums and cur <= win_nums[-1]):
            print(win_nums, cur)
            if(win_nums[-1] == cur):
                answer[0] += 1
                answer[1] += 1
            win_nums.pop()
                
    return [rank[answer[1]], rank[answer[0]]]