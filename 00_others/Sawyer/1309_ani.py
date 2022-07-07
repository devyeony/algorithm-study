import sys
input = sys.stdin.readline

result = []

n = int(input())

result = [[0,0,0] for _ in range(n) ]

result[0] = [1,1,1]

for i in range(1,n) :
    result[i][0] = result[i-1][0] + result[i-1][1] + result[i-1][2] 
    result[i][1] = result[i-1][0] + result[i-1][2] 
    result[i][2] = result[i-1][0] + result[i-1][1] 
    
    result[i-1] = []
    
print(sum(result[n-1])%9901)
