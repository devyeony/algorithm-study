import sys 

input = sys.stdin.readline


N,M = map(int,input().split())

dic = {}
for i in range(N) :
    dic[str(i+1)] = str(input().rstrip())


dicto = {v:k for k,v in dic.items()} 



for _ in range(M) :
    word = str(input().rstrip())
    if word in dic :
        print(dic[word])
    else :
        print(dicto[word])  