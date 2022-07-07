import sys
input = sys.stdin.readline


N = int(input())

S = []

for _ in range(N) :
    words = input().strip().split()
    
    if len(words) > 1 :
        word = words[0]
        num = int(words[1])
    else :
        word = words[0]
        

    if word == 'add' :
        if num not in S : 
            S.append(int(num))
    
    elif word == 'remove' :
        if num in S :
            S.remove(num)
    elif word == 'check' :
        if num in S :
            print(1)
        else :
            print(0)
    elif word == 'toggle' :
        if num in S :
            S.remove(num)
        else :
            S.append(num)
    elif word == 'all' :
        S = [k for k in range(1,21)]
    elif word == 'empty' :
        S = []