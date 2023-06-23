from collections import Counter
def solution(clothes):
    categoryList = []
    for name, category in clothes:
        categoryList.append(category)
        
    answer = 1
    categoryList = Counter(categoryList)
    for a in categoryList:
        answer *= (categoryList[a]+1)
    
    return answer - 1