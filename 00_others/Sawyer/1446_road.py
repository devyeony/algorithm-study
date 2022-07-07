import sys

input = sys.stdin.readline



N, D = map(int,input().split())

value = [[] for _ in range(10001)] # arrival, value

distance = [i for i in range(D+1)]

for _ in range(N) :
    
    start,arrival,value = map(int,input().split())
    value[start].append([arrival,value])




for i in range(D+1) :
    if i != 0 :
        distance[i] = min(distance[i-1]+1, distance[i])
    for j in value[i]:
        if j[0] <= D and distance[j[0]] > distance[i]+j[1] :
            distance[j[0]] = distance[i]+j[1]

            
            
            
print(distance[D])
    


    
