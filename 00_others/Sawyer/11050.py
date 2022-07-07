

import sys 
input = sys.stdin.readline

import math


N,K = map(int, input().split())


result = math.factorial(N)/ (math.factorial(K)*math.factorial(N-K))

print(int(result))