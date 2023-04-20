def solution(s):
    
    cnt1 = cnt2 = 0
    while(s != '1'):
        cnt2 += len(s) - s.count('1')
        s = bin(s.count('1'))[2:]
        cnt1 += 1
        print(s)
    return [cnt1, cnt2]