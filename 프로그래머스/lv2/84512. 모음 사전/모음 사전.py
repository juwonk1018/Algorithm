def solution(word):
    def getSequence(letter):
        vowels = ["A", "E", "I", "O", "U"]
        seq = [letter]
        
        if(len(letter) < 5):
            for vowel in vowels:
                seq += getSequence(letter + vowel)
        
        return seq
    
    dictOrder = getSequence("")
    return dictOrder.index(word)