def solution(s):
    answer = ''
    capital = True
    for letter in s:
        if(letter.isdigit()):
            answer += letter
            capital = False
            
        elif(letter.isalpha() and capital):
            answer += letter.upper()
            capital = False
        
        elif(letter.isalpha() and not(capital)):
            answer += letter.lower()
        
        elif(letter == ' '):
            capital = True
            answer += letter
    
    return answer