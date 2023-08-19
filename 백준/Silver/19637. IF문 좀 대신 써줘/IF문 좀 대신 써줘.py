import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nameList = []
powerList = []

for _ in range(n):
    name, power = input().split()
    nameList.append(name)
    powerList.append(int(power))

characters = []
for _ in range(m):
    characters.append(int(input()))

characterName = dict()

idx = 0
for character in sorted(characters):
    while(character > powerList[idx]):
        idx += 1

    if(character <= powerList[idx]):
        characterName[character] = nameList[idx]

for character in characters:
    print(characterName[character])