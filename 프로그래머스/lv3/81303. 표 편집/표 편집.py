def solution(n, k, cmd):
    
    answer = ["O"] * n
    
    beforeNextPointer = [[i-1, i+1] for i in range(n)]
    selectedRow = k

    recentDeletedRow = []
    
    for command in cmd:
        command = command.split()
        if(command[0] == 'U'):
            for i in range(int(command[1])):
                selectedRow = beforeNextPointer[selectedRow][0]
                
        elif(command[0] == 'D'):
            for i in range(int(command[1])):
                selectedRow = beforeNextPointer[selectedRow][1]
                
        elif(command[0] == 'C'):
            answer[selectedRow] = "X"
            recentDeletedRow.append(selectedRow)
            
            beforeRow = beforeNextPointer[selectedRow][0]
            nextRow = beforeNextPointer[selectedRow][1]
            
            if(0 <= beforeRow < n):
                beforeNextPointer[beforeRow][1] = beforeNextPointer[selectedRow][1]
            
            if(0 <= nextRow < n):
                beforeNextPointer[nextRow][0] = beforeNextPointer[selectedRow][0]
            
            prevRow = selectedRow
            
            if(beforeNextPointer[selectedRow][1] < n):
                selectedRow = beforeNextPointer[selectedRow][1]
            else:
                selectedRow = beforeNextPointer[selectedRow][0]
            
            
        elif(command[0] == 'Z'):
            num = recentDeletedRow.pop()
            answer[num] = "O"
            
            beforePointer, nextPointer = beforeNextPointer[num][0], beforeNextPointer[num][1]
            
            if(0 <= beforePointer < n):
                beforeNextPointer[beforePointer][1] = num
            
            if(0 <= nextPointer < n):
                beforeNextPointer[nextPointer][0] = num
                
    return ''.join(answer)