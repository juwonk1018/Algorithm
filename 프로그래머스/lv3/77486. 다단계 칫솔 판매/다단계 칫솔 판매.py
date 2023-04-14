from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    parent = [0] * len(enroll)
    num = dict()
    
    for i in range(len(enroll)): # 부모가 누군지 저장
        num[enroll[i]] = i
        if(referral[i] != "-"):
            parent[i] = num[referral[i]]
        else:
            parent[i] = -1
        
    sell = defaultdict(list)
    for i in range(len(seller)):
        sell[num[seller[i]]].append(amount[i] * 100)
        
    for person, moneyList in sell.items():
        for money in moneyList:
            cur = person
            while(cur != -1 and money != 0):
                parentMoney = money // 10
                answer[cur] += money - parentMoney
                money = parentMoney; cur = parent[cur]
                
            
    
    return answer