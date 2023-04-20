def solution(weights):
    weight_num = [0] * 1001
    for weight in weights:
        weight_num[weight] += 1
    answer = 0
    for i in range(100, 1001):
        if(weight_num[i] > 1):
                answer += weight_num[i]*(weight_num[i]-1)/2 #몸무게가 같은 사람들의 경우의 수
        
        for j in range(i+1, 1001): # i < j
            if(i*3 == j*2 or i*2 == j or i*4 == j*3):
                answer += weight_num[i] * weight_num[j]
    
    return answer