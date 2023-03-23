# 23일 10:45 ~

def solution(commands):
    size = 50
    graph = [['EMPTY'] * (size+1) for _ in range(size+1)]
    
    mergeList = []
    mergeValue = []
    answer = []
    
    for line in commands:
        line_to_list = line.split()
        command, value = line_to_list[0], line_to_list[1:]
        
        if(command == 'UPDATE'): # 병합 후 UPDATE도 확인
            valueLength = len(value) 
            if(valueLength == 3): # UPDATE r c value
                r, c, string = int(value[0]), int(value[1]), value[2]
                found = False
                for i in range(len(mergeList)): # 병합된 셀이라면 병합된 값을 바꾸기
                    if([r,c] in mergeList[i]):
                        mergeValue[i] = string
                        found = True
                
                if(not(found)):
                    graph[r][c] = string
                    
            else: # UPDATE value1 value2 
                value1, value2 = value
                for k in range(len(mergeValue)): # 병합된 셀 탐색
                    if(mergeValue[k] == value1):
                        mergeValue[k] = value2
                
                for i in range(1, size+1): # 셀 탐색
                    for j in range(1, size+1):
                        if(graph[i][j] == value1):
                            graph[i][j] = value2
        
        elif(command == 'MERGE'):
            r1, c1, r2, c2 = map(int, value)
            if(r1 == r2 and c1 == c2): # 셀이 같은 경우
                continue
            
            else:
                idx1, idx2 = -1, -1
                for i in range(len(mergeList)): # 병합 여부를 확인
                    if([r1, c1] in mergeList[i]):
                        idx1 = i
                    if([r2, c2] in mergeList[i]):
                        idx2 = i
                
                if(idx1 == -1 and idx2 != -1): # (r2, c2)가 merge된 상태
                    mergeList[idx2] += [[r1, c1]] # 기존의 값에 삽입
                    if(graph[r1][c1] != 'EMPTY'): # (r1, c1)의 값이 비어있지 않다면 값을 옮김
                        mergeValue[idx2] = graph[r1][c1]        
                    
                elif(idx1 != -1 and idx2 == -1): # (r1, c1)가 merge된 상태
                    mergeList[idx1] += [[r2, c2]]
                    if(mergeValue[idx1] == 'EMPTY'):
                        mergeValue[idx1] = graph[r2][c2]
                    
                elif(idx1 != -1 and idx2 != -1): # 모두 merge
                    if(idx1 != idx2):
                        mergeList[idx1] += mergeList[idx2]
                        if(mergeValue[idx1] == 'EMPTY'):
                            mergeValue[idx1] = mergeValue[idx2]

                        mergeList.pop(idx2)
                        mergeValue.pop(idx2)
                elif(idx1 == -1 and idx2 == -1): # 둘 다 병합되지 않으면, 새로운 mergeList를 추가
                    if(graph[r1][c1] != 'EMPTY'):
                        mergeValue.append(graph[r1][c1])
                    else:
                        mergeValue.append(graph[r2][c2])
                        
                    mergeList.append([[r1,c1], [r2,c2]])
                
                graph[r1][c1] = 'EMPTY'
                graph[r2][c2] = 'EMPTY'
                
        elif(command == 'UNMERGE'):
            r, c = int(value[0]), int(value[1])
            
            for i in range(len(mergeList)):
                if([r,c] in mergeList[i]):
                    graph[r][c] = mergeValue[i]
                    mergeList.pop(i)
                    mergeValue.pop(i)
                    break
            
        elif(command == 'PRINT'):
            r, c = int(value[0]), int(value[1])
            
            val = graph[r][c]
            if(val == 'EMPTY'):
                ans = 'EMPTY'
                for i in range(len(mergeList)):
                    if([r,c] in mergeList[i]):
                        ans = mergeValue[i]
                        break
                answer.append(ans)
            else:
                answer.append(val)
    
    return answer