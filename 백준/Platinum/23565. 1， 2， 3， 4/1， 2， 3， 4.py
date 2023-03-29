import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())

    if(d): # d가 존재
        ans = d+1 # [0,4,8,12,16,20 ...]
        
        # 2의 배수 처리

        if(b):
            # [b, d], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
            # [b+, d], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 ...]
            ans = ans * 2 + (b-1)
        else:
            pass

        # 1의 배수 처리
        if(a): 
            if(b): # 2의 배수 모두 존재
                ans += ans + (a-1)
            else: # 4의 배수만 존재
                ans += ans * min(3, a)
                if(a > 3):
                    ans += a-3
        
        # 3의 배수 처리
        if(c): #c, d가 존재
            if(b==0):
                if(a==0): #c,d만 존재
                    if(c<=3): #문제?
                        ans += ans * c
                    else: # d가 1이면, [0, 4]인 모양
                        if(d==1):
                            ans += ans * 3 + (c-3)*2
                        else:
                            ans += ans * 3 + (c-3)*3
                elif(a==1):
                    if(c<=2):
                        ans += (ans//2 + 1) * c
                    else:
                        ans += (ans//2 + 1) * 2 + 3 * (c-2)
                    
                elif(a==2):
                    ans += (ans//3) + 2 + 3 * (c-1)
                elif(a>=3):
                    ans += 3 * c
            
            elif(b>=1):
                if(a == 0): #[1, 0, 1, 0, 1]
                    ans += ans + 3 * (c-1)
                else: #[1, 1, 1, 1, 1]
                    ans += 3 * c


    else:
        if(c >= 1): #c,b, a
            ans = c+1
            if(a <= 1):
                if(a == 0 and b == 0):
                    ans = ans
                elif(a == 0 and b >= 1):
                    ans += ans * min(2, b)
                    if(b >= 3):
                        ans += 2 * (b-2)

                elif(a == 1 and b == 0):
                    ans = ans * 2

                elif(a == 1 and b >= 1):
                    ans = (b+1) * 2 + 3 * c
                            
            elif(a >= 2):
                ans = ans * 3 + (a-2) + b * 2


        else: #b,a
            if(b==0): #a
                ans = a + 1
            else:
                if(a==0): # b
                    ans = b + 1
                else: # a, b
                    ans = (b + 1) * 2 + (a-1)


    print(ans)
