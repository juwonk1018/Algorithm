import sys
n, k = map(int, input().split())

table = list(input().strip())


for i in range(n):
    if(table[i] == 'P'):
        for j in range(-k, k+1):
            if(0 <= i+j < n and table[i+j] == 'H'):
                table[i+j] = 'E'
                break

print(table.count("E"))