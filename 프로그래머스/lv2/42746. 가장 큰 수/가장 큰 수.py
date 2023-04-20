def solution(numbers):
    # 31, 312 경우 생각
    
    arr = []
    for number in numbers:
        arr.append([(str(number) * 3)[:4], number])
    arr.sort(reverse=True, key = lambda x : [x[0], -x[1]])
    
    answer = ''
    for element in arr:
        answer += str(element[1])
    return str(int(answer))

