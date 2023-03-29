# 뒤에서 순차적으로 탐색 시, n = 100000이고 대부분의 택배가 처음 부분에 몰려 있다면 시간 길어짐. => 택배가 존재하는 리스트 작성

def solution(cap, n, deliveries, pickups):
    deliveryList = []
    pickupList = []
    
    for i in range(n):
        if deliveries[i]:
            deliveryList.append(i)
        if pickups[i]:
            pickupList.append(i)
            
    answer = 0
    while(deliveryList or pickupList): # 트럭이 갈 상황이 존재한다면
        currentBundle = cap    
        
        distance = 0
        emptyBox = 0 # 수거할 박스, 뒤에서부터 search하면 택배를 다 내린 후 짐이 0인 상태부터 시작
        
        if(deliveryList):
            distance = max(deliveryList[-1] + 1, distance)
        while(deliveryList and currentBundle): # 짐을 배달
            housePos = deliveryList.pop()
            bundle = min(deliveries[housePos], currentBundle)
            
            deliveries[housePos] -= bundle 
            currentBundle -= bundle
            #짐이 남아있다면 다시 리스트에 추가
            if(deliveries[housePos]):
                deliveryList.append(housePos)
        
        if(pickupList):
            distance = max(pickupList[-1] + 1, distance)
        
        while(pickupList and emptyBox < cap): # 트럭이 비거나, 가져올 것이 있다면
            # 빈 박스 수거 : 공간이 존재하는지(cap-emptyBox) 확인
            housePos = pickupList.pop()
            box = min(pickups[housePos], cap - emptyBox)
            emptyBox += box
            pickups[housePos] -= box
            
            if(pickups[housePos]):
                pickupList.append(housePos)
        
        answer += distance * 2 # 왕복

    return answer