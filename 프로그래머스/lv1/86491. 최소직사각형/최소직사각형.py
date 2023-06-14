def solution(sizes):
    width = []
    length = []
    for w, l in sizes:
        width.append(w)
        length.append(l)
        
    if(max(width) > max(length)):
        walletWidth = max(width)
        walletLength = 0
        for i in range(len(sizes)):
            walletLength = max(walletLength, min(width[i], length[i]))
    else:
        walletLength = max(length)
        walletWidth = 0
        for i in range(len(sizes)):
            walletWidth = max(walletWidth, min(width[i], length[i]))
        
    answer = walletLength * walletWidth
    return answer