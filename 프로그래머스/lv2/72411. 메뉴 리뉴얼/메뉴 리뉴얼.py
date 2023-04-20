from itertools import combinations
from collections import defaultdict, Counter
def solution(orders, course):
    answer = []
    for c in course:
        count = defaultdict(int); MAX = 0
        for order in orders:
            for element in combinations(order, c):
                courseCandidate = ''.join(sorted(element))
                count[courseCandidate] += 1
                MAX = max(count[courseCandidate], MAX)

        for string, n in count.items():
            if(count[string] == MAX and MAX >= 2):
                answer.append(string)

    answer.sort()
    return answer