n = int(input())  

for i in range(n):
    reg, out = map(str, input().split())
    reg = reg.zfill(4)
    out = out.zfill(4)
    arr = [["",reg]]
    visited = [0] * 10000
    ans = ""
    while(ans == ""):
        new_arr = []
        for element in arr:
            new_reg = element[1][1:] + element[1][0]
            new_seq = element[0] + "L"

            if(visited[int(new_reg)] == 0):
                visited[int(new_reg)] = 1
                new_arr.append([new_seq, new_reg])
                if(new_reg == out):
                    ans = new_seq
                    break
            
            new_reg = element[1][3] + element[1][0:3]
            new_seq = element[0] + "R"

            if(visited[int(new_reg)] == 0):
                visited[int(new_reg)] = 1
                new_arr.append([new_seq, new_reg])
                if(new_reg == out):
                    ans = new_seq
                    break

            new_reg = str(int(element[1])*2 % 10000).zfill(4)
            new_seq = element[0] + "D"

            if(visited[int(new_reg)] == 0):
                visited[int(new_reg)] = 1
                new_arr.append([new_seq, new_reg])
                if(new_reg == out):
                    ans = new_seq
                    break
                
            if(int(element[1]) == 0):
                new_reg = str(9999)
            else:
                new_reg = str(int(element[1])-1).zfill(4)
            new_seq = element[0] + "S"

            if(visited[int(new_reg)] == 0):
                visited[int(new_reg)] = 1
                new_arr.append([new_seq, new_reg])
                if(new_reg == out):
                    ans = new_seq
                    break
        arr = new_arr
    
    print(ans)


"""
1. visited[0] * 10000을 통해, 방문한 number를 기록하여 LLLL, RRRR 등의 원점으로 돌아오는 command를 제거
2. D=,S=,L=,R= 에 값을 저장해, for x, op in ((D, op + 'D'), (S, op + 'S'), (L, op + 'L'), (R, op + 'R')): 를 이용해 append 가능
"""