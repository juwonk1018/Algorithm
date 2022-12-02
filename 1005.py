import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

tc = int(input())

def mintime(num, complete_time):
    if(complete_time[num] == -1):
        ans = []
        if(prebuild[num]):
            for element in prebuild[num]:
                ans.append(mintime(element, complete_time) + time[num])
            complete_time[num] = max(ans)
        else:
            complete_time[num] = time[num]
    
    return complete_time[num]

    

for _ in range(tc):
    building_num, rule_num = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    prebuild = [[] for _ in range(building_num+1)]
    complete_time = [-1] * (building_num+1)

    for _ in range(rule_num):
        a, b = map(int, input().split())
        prebuild[b].append(a)
    
    dest = int(input())

    print(mintime(dest, complete_time))
        
