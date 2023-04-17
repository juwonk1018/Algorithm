def solution(s):
    s = s.replace("{", "")
    s = list(s.split("}"))
    s = sorted(s, key = lambda x: len(x))
    
    answer = []
    for element in s:
        for num in element.split(","):
            if(num != '' and num not in answer):
                answer.append(num)
                break
    
    return list(map(int, answer))