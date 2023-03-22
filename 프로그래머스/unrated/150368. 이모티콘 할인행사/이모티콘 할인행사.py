from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    for discountList in product([10,20,30,40], repeat=len(emoticons)): # 각 할인율마다 확인
        emoticonPlus, income = 0, 0
        for target_discount, target_money in users:
            total = 0
            for i in range(len(discountList)): #모든 이모티콘을 검색   
                if(target_discount <= discountList[i]): #만족하는 할인율이 있다면
                    total += emoticons[i] * (100 - discountList[i])/100
            
            if(total >= target_money):
                emoticonPlus += 1
            else:
                income += total
        
        if(emoticonPlus > answer[0]):
            answer = [emoticonPlus, income]
        elif(emoticonPlus == answer[0]):
            answer = [answer[0], max(answer[1], income)]
    
    return answer