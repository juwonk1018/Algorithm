def f(number):
    numberToBinary = bin(number)[2:].zfill(100)
    for i in range(len(numberToBinary)-1, -1, -1):
        if(numberToBinary[i] == '0'):
            numberToBinary = numberToBinary[:i] + '1' + numberToBinary[i+1:]
            for j in range(i+1, len(numberToBinary)):
                if(numberToBinary[j] == '1'):
                    numberToBinary = numberToBinary[:j] + '0' + numberToBinary[j+1:]
                    break
            return int('0b'+numberToBinary, 2)

def solution(numbers):
    answer = [f(number) for number in numbers]
    return answer