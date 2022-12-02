n = int(input())
m = int(input())
str = input().strip()

cnt = 0
repeat = 0
i=1
while(i < m-1):
    if(str[i-1] == 'I' and str[i] == 'O' and str[i+1] == 'I'):
        repeat +=1
        i+=1
        if(repeat == n):
            cnt +=1
            repeat -=1
    else:
        repeat = 0
        
    i+=1
print(cnt)