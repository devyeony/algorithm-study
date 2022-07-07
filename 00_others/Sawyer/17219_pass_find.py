import sys

input = sys.stdin.readline 

N,M = map(int,input().split())

dic = {}

for _ in range(N) :
    X, Y = map(str,input().split())
    dic[X] = Y

for _ in range(M) :
    print(dic[str(input())[:-1]])
    