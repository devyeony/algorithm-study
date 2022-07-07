import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

result = deque()

for _ in range(n) :
    word = list(map(str,input().split()))
    if word[0] == 'push' :
        result.append(word[1])
    elif word[0] == 'pop' :
        if result :
            print(result.pop())
        else :
            print(-1)
    elif word[0] == 'size' :
        print(len(result))
    elif word[0] == 'empty' :
        if len(result) == 0 :
            print(1)
        else :
            print(0)
    elif word[0] == 'top' :
        if result :
            print(result[-1])
        else :
            print(-1)