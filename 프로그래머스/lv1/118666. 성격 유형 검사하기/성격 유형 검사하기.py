from collections import defaultdict
def solution(survey, choices):
    typeScore = defaultdict(int)
    
    for i in range(len(survey)):
        score = choices[i] - 4
        if(score > 0):
            typeScore[survey[i][1]] += score
        else:
            typeScore[survey[i][0]] += abs(score)
            
    typeList = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    answer = ''
    for type1, type2 in typeList:
        if(typeScore[type1] >= typeScore[type2]):
            answer += type1
        else:
            answer += type2
    return answer