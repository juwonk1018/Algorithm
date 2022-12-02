m,n,h = map(int, input().strip().split())
tomato = []
ripen = []
for i in range(n*h):
    temp = list(map(int, input().strip().split()))
    for j in range(len(temp)):
        if(temp[j]==1):
            ripen.append([i,j])
    tomato.append(temp)
        
changed = True
count = 0

while(ripen):
    next_ripen = []
    for k in ripen:
        #ROW
        if(k[0] % n != 0 and tomato[k[0] - 1][k[1]] == 0):
            tomato[k[0] - 1][k[1]] = 1
            #if([k[0] - 1,k[1]] not in next_ripen):
            next_ripen.append([k[0] - 1,k[1]])
        if((k[0]-n+1) % n != 0 and tomato[k[0] + 1][k[1]] == 0):
            tomato[k[0] + 1][k[1]] = 1
            #if([k[0] + 1,k[1]] not in next_ripen):
            next_ripen.append([k[0] + 1,k[1]])

        #COL
        if(k[1] % m != 0 and tomato[k[0]][k[1] -1] == 0):
            tomato[k[0]][k[1] - 1] = 1
            #if([k[0],k[1] - 1] not in next_ripen):
            next_ripen.append([k[0],k[1] - 1])
        if((k[1]-m+1) % m != 0 and tomato[k[0]][k[1] + 1] == 0):
            tomato[k[0]][k[1] + 1] = 1
            #if([k[0],k[1] + 1] not in next_ripen):
            next_ripen.append([k[0],k[1] + 1])
        #BOX
        if(k[0] - n >= 0 and tomato[k[0] - n][k[1]] == 0):
            tomato[k[0] - n][k[1]] = 1
            #if([k[0] - n,k[1]] not in next_ripen):
            next_ripen.append([k[0] - n,k[1]])
        if(k[0] + n < n*h and tomato[k[0] + n][k[1]] == 0):
            tomato[k[0] + n][k[1]] = 1
            #if([k[0] + n,k[1]] not in next_ripen):
            next_ripen.append([k[0] + n,k[1]])
    set_ripen = set(map(tuple,next_ripen))
    ripen = list(set_ripen)
    if(next_ripen):
        count +=1

for i in range(n*h):
    for j in range(m):
        if(tomato[i][j] == 0):
            count = -1
print(count)

''' in 보다는 tuple을 이용해 []를 비교하는 set으로 중복제거'''