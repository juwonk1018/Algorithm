a,b,c = map(int, input().split())

def divide(start,end):
    mid = (start+end)//2
    if( end - start == 1):
        return a%c
    if( (end-start) % 2 == 0):
        temp = (pow(divide(start,mid),2)) % c
        return temp
    elif( (end-start) % 2 == 1):
        temp = (pow(divide(start,mid),2) * a) %c
        return temp
    
result = divide(0,b) 
print(result%c)

"""
pow(a,b,c)도 가능..."""