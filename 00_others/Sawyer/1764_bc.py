import sys


input = sys.stdin.readline

N,M = map(int,input().split())


a = set()
for _ in range(N) :
    a.add(input().rstrip())
    
b = set()

for _ in range(M) :
    b.add(input().rstrip())
    
    


c = sorted(list(a & b))
print(len(c))
          
for _ in c :
    print(_)