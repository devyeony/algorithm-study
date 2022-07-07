import sys

for i in sys.stdin.readlines() :
    
    N,M = i.split()

    N = int(N)
    result = ''

    for j in M:
        result += j*N 
    print(result)