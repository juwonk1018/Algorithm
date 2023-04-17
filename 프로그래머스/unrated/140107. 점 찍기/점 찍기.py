def solution(k, d):
    ans = 0
    for i in range(0,d+1, k):
        ans += ((d**2-i**2)**(1/2)) // k + 1
    return ans