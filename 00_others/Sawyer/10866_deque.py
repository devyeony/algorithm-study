import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

result = deque()

for _ in range(n) :
    word = list(map(str,input().split()))
    if word[0] == 'push_front' :
        result.appendleft(word[1])
    elif word[0] == 'push_back' :
        result.append(word[1])
    elif word[0] == 'pop_front' :
        if result :
            print(result.popleft())
        else :
            print(-1)
    elif word[0] == 'pop_back' :
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
    elif word[0] == 'front' :
        if result :
            print(result[0])
        else :
            print(-1)
    elif word[0] == 'back' :
        if result :
            print(result[-1])
        else :
            print(-1)