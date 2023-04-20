def solution(citations):
    citations.sort(reverse = True)
    for i in range(1, len(citations)+1):
        if(citations[i-1] >= i):
            continue
        else:
            return i-1
    return i