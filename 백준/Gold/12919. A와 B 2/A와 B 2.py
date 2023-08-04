s = input().strip()
t = input().strip()


q = [t]
for i in range(len(t)-len(s)):
    nq = set()
    
    while(q):
        cur = q.pop()
        if(cur[0] == 'B' and cur[-1] == 'A'):
            nq.add(cur[:-1])
            nq.add((cur[1:])[::-1])

        elif(cur[0] == 'A' and cur[-1] == 'A'):
            nq.add(cur[:-1])

        elif(cur[0] == 'B' and cur[-1] == 'B'):
            nq.add((cur[1:])[::-1])

    q = list(nq)

print(1 if s in q else 0)