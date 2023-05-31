def solution(n, lost, reserve):
    clothNumber = [0] + [1] * n
    
    for num in lost:
        clothNumber[num] -= 1
    for num in reserve:
        clothNumber[num] += 1
    
    answer = [0] * (n+1)
    
    for i in range(1, n+1):
        studentNumber = [i-1, i+1]
        if(clothNumber[i]):
            answer[i] = 1
        for number in studentNumber:
            if(clothNumber[i] == 2 and 1 <= number <= n and clothNumber[number] == 0):
                clothNumber[number] += 1
                clothNumber[i] -= 1
                
                answer[number] = 1
    
    return sum(answer)