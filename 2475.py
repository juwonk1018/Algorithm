temp = [0,1,4,9,16,25,36,49,64,81]
arr = list(map(int,input().split()))
print(sum([temp[arr[i]] for i in range(5)])%10)
