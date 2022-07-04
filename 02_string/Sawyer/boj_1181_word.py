import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

words = []

for _ in range(N) :
    words.append(str(input().strip()))

words = list(set(words))

words.sort()

words.sort(key =len)


for i in words :
    print(i)