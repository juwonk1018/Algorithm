# list, deque간 변환에 시간이 많이 소모되었는데, inner에도 list가 아닌 deque를 넣음으로써 시간 문제 해결

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
                    
            r.rotate(1)
            l.rotate(1)
            
        if(operation == "Rotate"):
            if(u):
                u.appendleft(l.popleft())
                r.appendleft(u.pop())
                d.append(r.pop())
                l.append(d.popleft())
            else:
                r.appendleft(l.popleft())
                l.append(r.pop())
    
    l_list = [[num] for num in list(l)]
    mid_list = [list(u)] + [list(inner[i]) for i in range(R-2)] + [list(d)]
    r_list = [[num] for num in list(r)]
    
    answer = []
    for left, mid, right in zip(l_list, mid_list, r_list):
         answer.append(left + mid + right)
#     if(u):
#         answer.append([l[0]] + list(u) + [r[0]])
#         if(inner):
#             for i in range(len(inner)):
#                 answer.append([l[i+1]] + list(inner[i]) + [r[i+1]])
#         answer.append([l[R-1]] + list(d) + [r[R-1]])
#     else:
#         for i in range(R):
#             answer.append([l[i], r[i]])
            
    return answer