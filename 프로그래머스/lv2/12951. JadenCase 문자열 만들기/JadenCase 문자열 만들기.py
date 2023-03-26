def solution(s):
    answer = ''
    capital = True
    for letter in s:
        if('0' <= letter <= '9'):
            answer += letter
            capital = False
        if('a' <= letter <= 'z' and capital):
            answer += letter.upper()
            capital = False
        elif('a' <= letter <= 'z' and not(capital)):
            answer += letter
            
        if('A' <= letter <= 'Z' and not(capital)):
            answer += letter.lower()
        elif('A' <= letter <= 'Z' and capital):
            answer += letter
            capital = False
        
        if(letter == ' '):
            capital = True
            answer += letter
    
    return answer