# 첫번째 시도, 수빈이의 위치를 매 시간마다 +1, -1, *2인 위치를 list에 저장해서 계속 진행
# => 34%에서 시간초과 : 최적화를 더 잘해야됨, 이분 탐색도 불가능 (해당 시점에서 더 가면 만나지 않을 수 있음)

# 두번째 시도, 동생이 t만큼의 시간을 지나서 해당 위치에 존재한다면, t번의 -1, +1, /2를 이용해 갈 수 있는 위치를 조회
# => 시간 많이걸림

# 동생은 t가 1000안에 무조건 찾아야됨 : 1~1000초까지 더하면 500,500초
# 짝수, 홀수차를 나누면 t-2번째에 방문한 것을 똑같이 방문

n, k = map(int, input().split())

# 동생이 t초 후에 이동할 때에는 t가 짝수면 현재 위치에서 t까지 거리의 +-t 


yPos = k # 동생 위치
time = 0

visited_o = [0] * 500001 #홀수차 방문여부
visited_e = [0] * 500001 #짝수차 방문여부

odd_pos = set() # 수빈이가 홀수차에 갈 수 있는 위치
even_pos = set([n]) # # 수빈이가 짝수차에 갈 수 있는 위치

if(n == k):
    print(time)

else:
    while(True):
        time += 1
        yPos += time # 동생의 이동
        
        if(yPos > 500000): #범위를 넘어선다면
            print(-1)
            break
        
        new_cur = []
        if(time % 2 == 1):
            for pos in even_pos: # 홀수차 수빈이의 이동
                if(0 <= pos+1 <= 500000 and visited_o[pos+1] == 0):
                    visited_o[pos+1] = 1
                    new_cur.append(pos + 1)
                if(0 <= pos-1 <= 500000 and visited_o[pos-1] == 0):
                    visited_o[pos-1] = 1
                    new_cur.append(pos - 1)
                if(0 <= pos*2 <= 500000 and visited_o[pos*2] == 0):
                    visited_o[pos*2] = 1
                    new_cur.append(pos * 2)
            nextPos = set(new_cur)
            odd_pos = nextPos
            if(visited_o[yPos]):
                print(time)
                break
        elif(time % 2 == 0):
            for pos in odd_pos: # 짝수차 수빈이의 이동
                if(0 <= pos+1 <= 500000 and visited_e[pos+1] == 0):
                    visited_e[pos+1] = 1
                    new_cur.append(pos + 1)
                if(0 <= pos-1 <= 500000 and visited_e[pos-1] == 0):
                    visited_e[pos-1] = 1
                    new_cur.append(pos - 1)
                if(0 <= pos*2 <= 500000 and visited_e[pos*2] == 0):
                    visited_e[pos*2] = 1
                    new_cur.append(pos * 2)
                
            nextPos = set(new_cur)
            even_pos = nextPos
            if(visited_e[yPos]):
                print(time)
                break