import sys

input = sys.stdin.readline




T = int(input())


result = [[0] * 31 for _ in range(31)]

for j in range(1,31) :
    for k in range(j,31) :
        if j == k :
            result[j][k] = 1
        elif j == 1 :
            result[j][k] = k
        else:
            answer = 0
            for l in range(j-1,k):
                answer += result[j-1][l]
            result[j][k] = answer
                

for i in range(T) :
    bridge = list(map(int,input().split()))
    
    west = bridge[0]
    east = bridge[1]
    print(result[west][east])