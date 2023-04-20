from collections import defaultdict
def solution(name, yearning, photo):
    score = defaultdict(int)
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    answer = []
    for people in photo:
        total = 0
        for person in people:
            total += score[person]
        answer.append(total)
    
    return answer