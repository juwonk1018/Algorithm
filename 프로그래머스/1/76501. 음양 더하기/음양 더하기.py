def solution(absolutes, signs):
    return sum([number if sign else -1*number for number, sign in zip(absolutes, signs)])
        