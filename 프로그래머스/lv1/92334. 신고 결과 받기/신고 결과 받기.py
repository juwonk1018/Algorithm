from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    count = defaultdict(list)
    
    for r in list(set(report)): # 중복 제거
        s, d = r.split()
        count[d].append(s)
    
    for user in count:
        if(len(count[user]) >= k):
            for u in count[user]:
                answer[id_list.index(u)] += 1
                
    return answer