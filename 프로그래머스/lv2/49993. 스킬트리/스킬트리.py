def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skillStack = []
        for s in skill_tree:
            if(s in skill):
                if(skill[len(skillStack)] == s):
                    skillStack.append(s)
                else:
                    answer -= 1
                    break
                    
        answer += 1
        
    return answer