from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons, len(dungeons)):
        cur_k = k
        cnt = 0
        for req, consume in i:
            if(req <= cur_k):
                cur_k -= consume
                cnt += 1
                
        answer = max(cnt, answer)
    
    return answer