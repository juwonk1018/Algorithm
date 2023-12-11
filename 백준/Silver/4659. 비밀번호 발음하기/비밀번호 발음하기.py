import sys

input = sys.stdin.readline


while(True):
    password = input().strip()

    if(password == 'end'):
        break
    c1 = False
    c2 = c3 = True

    vowel = set(['a','e','i','o','u'])
    
    isVowel = True
    cnt = [0, 0] # Count : [consonant, vowel]

    for i in range(len(password)):
        if(password[i] in vowel):
            isVowel = True
            c1 = True
        else:
            isVowel = False

        cnt[isVowel] += 1
        cnt[not(isVowel)] = 0

        if(cnt[isVowel] >=3):
            c2 = False
            break

        if(i>0 and password[i] == password[i-1] and password[i] not in ['e','o']): # C3
            c3 = False
            break


    if(c1 and c2 and c3):
        print("<" + password + ">" + " is acceptable.")
    else:
        print("<" + password + ">" + " is not acceptable.")
