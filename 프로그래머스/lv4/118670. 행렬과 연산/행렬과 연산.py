from collections import deque

def solution(rc, operations):
    
    R = len(rc)
    C = len(rc[0])
    
    u = deque(rc[0][1:C-1])
    d = deque(rc[R-1][1:C-1])
    
    l = deque([]); r = deque([]); inner = deque([])
    
    for i in range(R):
        if(0 < i < R-1):
            inner.append(deque(rc[i][1:C-1]))
        r.append(rc[i][C-1])
        l.append(rc[i][0])
    
    for operation in operations:
        if(operation == "ShiftRow"):
            if(inner):
                inner.appendleft(u)
                u = d
                d = inner.pop()
            else:
                if(u and d):
                    u, d = d, u
                    
            r.appendleft(r.pop())
            l.appendleft(l.pop())
            
        if(operation == "Rotate"):
            if(u):
                u.appendleft(l.popleft())
                r.appendleft(u.pop())
                d.append(r.pop())
                l.append(d.popleft())
            else:
                r.appendleft(l.popleft())
                l.append(r.pop())
                
    answer = []
    
    if(u):
        answer.append([l[0]] + list(u) + [r[0]])
        if(inner):
            for i in range(len(inner)):
                answer.append([l[i+1]] + list(inner[i]) + [r[i+1]])
        answer.append([l[R-1]] + list(d) + [r[R-1]])
    else:
        for i in range(R):
            answer.append([l[i], r[i]])
            
    return answer