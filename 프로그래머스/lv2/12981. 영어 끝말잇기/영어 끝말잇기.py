def solution(n, words):
    w = set()
    prev = ""
    for i in range(len(words)):
        if(words[i] in w or (prev and words[i][0] != prev)):
            return [i%n+1, i//n+1]
        w.add(words[i])
        prev = words[i][-1]
        
    return [0,0]

    return answer