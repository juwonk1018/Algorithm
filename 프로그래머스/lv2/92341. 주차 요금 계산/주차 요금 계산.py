def solution(fees, records):
    parking = [-1] * 10000
    totalTime = [0] * 10000
    
    for record in records: # 출입 처리
        time, number, status = record.split()
        h, m = time.split(":")
        number = int(number)
        cur = int(h) * 60 + int(m) # 시간을 분으로 나타냄
        if(status == 'IN'):
            parking[number] = cur
        
        elif(status == 'OUT'):
            totalTime[number] += cur - parking[number]
            parking[number] = -1
    
    for i in range(10000): # 이후에 주차장에 차량이 남아있다면, 23:59까지 존재로 처리
        if(parking[i] != -1):
            totalTime[i] += (60 * 23 + 59 - parking[i])
            parking[i] = 0
    
    answer = []
    std, std_fee, add, add_fee = fees
    for i in range(10000):
        if(totalTime[i]):
            if(totalTime[i] > std):
                fee = std_fee + -(-(totalTime[i] - std) // add) * add_fee
            else:
                fee = std_fee
            answer.append(fee)
    
    return answer