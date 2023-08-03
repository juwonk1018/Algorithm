n, k = map(int, input().split())

n = str(n)
m = len(n)


s = [n]

for i in range(min(int(n), k)):

    ns = set()
    while(s):
        cur = s.pop()
        

        for i in range(m):
            for j in range(i+1,m):
                nw = cur[:i] + cur[j] + cur[i+1:j] + cur[i] + cur[j+1:]
                if(nw[0] != '0'):
                    ns.add(nw)
        
    s = list(ns)

print(max(s) if s else -1)