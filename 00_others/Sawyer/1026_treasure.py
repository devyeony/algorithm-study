import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

sort_b = sorted(B)
sort_a = sorted(A,reverse=True)


result = 0

for i in range(n) :
    result += sort_a[i] * sort_b[i]


print(result)