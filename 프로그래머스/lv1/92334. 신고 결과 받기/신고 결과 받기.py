from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    num = dict()
    count = defaultdict(list)
    for i, name in enumerate(id_list):
        num[name] = i
    
    for r in list(set(report)): # 중복 제거
        s, d = r.split()
        count[d].append(s)
    
    banUser = set()
    for user in count:
        if(len(count[user]) >= k):
            banUser.add(user)
            for u in count[user]:
                answer[num[u]] += 1
                
    
    return answer