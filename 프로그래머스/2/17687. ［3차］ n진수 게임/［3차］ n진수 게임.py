def solution(n, t, m, p):
    
    alphabet = ["A","B","C","D","E","F"]
    
    def dec_to_n(number, n): # number를 n진수로 변경
        
        if(number == 0):
            return "0"
        
        string = ""
        while(number):
            if(number % n < 10):
                string = str(number % n) + string
            elif(10 <= number % n <= 15):
                string = alphabet[number%n-10] + string
                
            number = (number - (number%n))//n
        
        return string
    
    cnt = 0
    result = ""
    while(len(result) <= m*t): # 전체 숫자를 저장
        result += dec_to_n(cnt, n)
        cnt += 1
    
    result = result[:m*t] # m*t번째 까지 절삭
    answer = result[p-1::m] # m번째 순서 도출
    return answer