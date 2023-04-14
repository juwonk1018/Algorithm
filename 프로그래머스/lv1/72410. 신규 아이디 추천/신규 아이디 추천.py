def solution(new_id):
    
    answer = ''
    for i in new_id.lower():
        if(i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.'):
            answer += i
    
    a = answer.replace("..", ".")
    while(answer != a):
        answer = a
        a = answer.replace("..", ".")
    if(answer != '' and answer[0] == '.'):
        answer = answer[1:]
    if(answer != '' and answer[-1] == '.'):
        answer = answer[:-1]
    
    if(answer == ''):
        answer = 'a'
    
    if(len(answer) >= 16):
        answer = answer[:15]
        
    if(answer != '' and answer[-1] == '.'):
        answer = answer[:-1]
    
    if(len(answer) <= 2):
        answer += answer[-1] * (3 - len(answer))
    return answer