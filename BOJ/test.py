from itertools import combinations

cnt = 0
for cur in combinations(range(10),3):
    cnt +=1

cnt2 = 0
for i in range(10):
     for j in range(i+1, 10):
         for k in range(j+1, 10):
             cnt2+=1

print(cnt, cnt2)