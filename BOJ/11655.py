import sys
input = sys.stdin.readline
string = input()

for i in range(0, len(string)):
    num = ord(string[i])
    if(num < 110 and num >= 97):
        print(chr(ord(string[i]) + 13), end = '')
    elif(num>=110):
        print(chr(ord(string[i]) - 13), end = '')

    elif(num>=78 and num <= 90):
        print(chr(ord(string[i]) - 13), end = '')
    elif(num<78 and num >= 65):
        print(chr(ord(string[i]) + 13), end = '')
    else:
        print(string[i], end = '')

    #print(chr(ord((string[i])-65+13)%26 + 65 if 65<=ord(i)<=90 else
    #(ord(string[i])-97+13)%26 + 97 if 97<=ord(i)<=122 else ord(i))

#l="abcdefghijklmnopqrstuvwxyz"
#h=l.upper(), s=l+h
#d=l[13:]+l[:13]+h[13:]+h[:13]
#t=str.maketrans(s,d)
#print(input().translate(t))

#문자열 처리 알아두기
