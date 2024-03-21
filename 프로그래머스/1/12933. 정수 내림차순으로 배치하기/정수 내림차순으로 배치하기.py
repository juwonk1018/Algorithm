def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    answer = int("".join(n))
    return answer