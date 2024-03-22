from collections import defaultdict
from itertools import product
def solution(user_id, banned_id):
    matched_id = defaultdict(set)
    for uid in user_id:
        for bid in banned_id:
            if(len(uid) == len(bid)):
                matched = True
                for i in range(len(uid)):
                    if(bid[i] != "*" and uid[i] != bid[i]):
                        matched = False
                        
                if(matched):
                    matched_id[bid].add(uid)
    
    bannedList = []
    
    for bid in banned_id:
        if(len(bannedList) == 0):
            for uid in matched_id[bid]:
                bannedList.append([uid])
        else:
            newBannedList = []
            for lst in bannedList:
                for uid in matched_id[bid]:
                    if(uid not in lst):
                        newBannedList.append(lst + [uid])
            bannedList = newBannedList  
    
    answer = set()
    for lst in bannedList:
        answer.add(tuple(sorted(lst)))
    
    return len(answer)