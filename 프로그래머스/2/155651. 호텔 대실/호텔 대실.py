def solution(book_time):
    answer = 0
    
    # 끝나는 시간에 10분 추가(청소 시간)
    for i in range(len(book_time)):
        start_time, end_time = book_time[i]
        e_h, e_m = map(int, end_time.split(":"))
        e_h, e_m = str((e_h*60+e_m+10)//60).zfill(2), str((e_h*60+e_m+10)%60).zfill(2)
        end_time = e_h+":"+e_m
        book_time[i] = [start_time, end_time]
        
    book_time.sort(key=lambda x:x[0])
    rooms = []
    for start_time, end_time in book_time:
        for i in range(len(rooms)):
            if(start_time >= rooms[i][-1][1]): # 퇴실 시간이 지났다면
                rooms[i].append([start_time, end_time])
                break
        else:
            rooms.append([[start_time, end_time]])
            
    answer = len(rooms)
    
    return answer