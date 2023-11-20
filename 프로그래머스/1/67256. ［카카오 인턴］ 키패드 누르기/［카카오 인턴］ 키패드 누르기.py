def solution(numbers, hand):
    leftThumb, rightThumb = [3,0], [3,2]
    leftNumber, midNumber, rightNumber = [1,4,7], [2,5,8,0], [3,6,9]
    answer = ''
    
    def getDistance(d1, d2): # distance 구하기
        return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])
    
    for number in numbers:
        if(number in leftNumber):
            leftThumb = [leftNumber.index(number), 0]
            answer += 'L'
        elif(number in rightNumber):
            rightThumb = [rightNumber.index(number), 0]
            answer += 'R'
        else:
            numberPosition = [midNumber.index(number), 1]
            leftDistance = getDistance(numberPosition, leftThumb)
            rightDistance = getDistance(numberPosition, rightThumb)
            
            if(leftDistance < rightDistance or (leftDistance == rightDistance) and hand == "left"):
                leftThumb = numberPosition
                answer += 'L'
            elif(leftDistance > rightDistance or (leftDistance == rightDistance) and hand == "right"):
                rightThumb = numberPosition
                answer += 'R'
    return answer