# functools 사용해서 풀어야 속도가 잘나옴.
# for i에서 i+=1 등은 안먹히는거 주의

import sys
import functools

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(input().split()[0])


ans = [arr[0]]

order = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
def compare(s1, s2): # s1 < s2 일 때 return 1
    i = j = 0
    while(i < len(s1)):
        if(j >= len(s2)): # 인덱스가 오버되었다면(s1의 길이가 긴 경우)
            return 1

        char_s1 = s1[i]
        char_s2 = s2[j]

        if(char_s1.isdigit()):
            for k in range(i+1, len(s1)):
                if(s1[k].isdigit()):
                    i = i+1
                    char_s1 += s1[k]
                else:
                    break
            
        if(char_s2.isdigit()):
            for k in range(j+1, len(s2)):
                if(s2[k].isdigit()):
                    j += 1
                    char_s2 += s2[k]
                else:
                    break
            
 
        if(char_s1.isdigit() and char_s2.isdigit()):
            if(int(char_s1) < int(char_s2)):
                return -1
            elif(int(char_s1) > int(char_s2)):
                return 1
            else:
                if(len(char_s1) < len(char_s2)):
                    return -1
                elif(len(char_s1) > len(char_s2)):
                    return 1
            
        elif(char_s1.isdigit() and not(char_s2.isdigit())):
            return -1
        
        elif(not(char_s1.isdigit()) and char_s2.isdigit()):
            return 1
        
        else:
            if(order.index(char_s1) < order.index(char_s2)): #우선순위가 높으면
                return -1
            elif(order.index(char_s1) > order.index(char_s2)): #우선순위가 낮으면
                return 1

        j += 1
        i += 1

    if(j < len(s2)):
        return -1 #j의 인덱스가 남았다면(s1의 길이가 짧은 경우)
    return 0

ans = sorted(arr, key=functools.cmp_to_key(compare))
print(*ans, sep = '\n')
