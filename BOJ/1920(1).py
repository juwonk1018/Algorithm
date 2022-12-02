"""while문으로 할 때는 시간초과, 함수를 def로 정의해서 recursion은 통과"""
import sys
input = sys.stdin.readline

m = int(input().strip())

arr = list(map(int, input().strip().split()))
arr.sort()

n = int(input().strip())

arr2 = list(map(int, input().strip().split()))

def binary(i,arr,start,end):
    if start > end:
        print("0")
        return 0
    mid = (start+end)//2
    if(arr[mid] > arr2[i]):
        binary(i, arr, start, mid-1)
    elif(arr[mid] < arr2[i]):
        binary(i, arr, mid+1, end)
    else:
        print("1")

for i in range(n):
    start = 0
    end = m-1

    binary(i,arr,start,end)
    

""" Set으로 풀기(set은 hash로 data를 찾아 in 함수가 O(1)에 작동
import sys
input = sys.stdin.readline

m = int(input().strip())

arr = set(list(map(int, input().strip().split())))

n = int(input().strip())

arr2 = list(map(int, input().strip().split()))


for i in arr2:
    print("1" if i in arr else "0")
"""
