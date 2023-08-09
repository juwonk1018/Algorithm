import sys
input = sys.stdin.readline

s = int(input())
switch = list(map(int, input().split()))

n = int(input())
for _ in range(n):
    g, number = map(int, input().split())

    if(g == 1):
        for i in range(number-1, s, number):
            switch[i] = (switch[i] + 1) % 2
    else:
        number -= 1
        switch[number] = (switch[number] + 1) % 2
        for i in range(1, s):
            if(0 <= number-i < number + i < s and switch[number-i] == switch[number+i]):
                switch[number-i] = (switch[number-i] + 1) % 2
                switch[number+i] = (switch[number+i] + 1) % 2
            else:
                break


for i in range(s//20+1):
    print(*switch[20*i:20*i+20])