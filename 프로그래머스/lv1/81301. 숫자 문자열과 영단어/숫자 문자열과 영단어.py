# 16:12 ~
def solution(s):
    wordToNumber = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i in range(10):
        s = s.replace(wordToNumber[i], str(i))
    
    return int(s)