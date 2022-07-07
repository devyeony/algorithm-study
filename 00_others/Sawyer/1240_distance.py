import sys
from collections import defaultdict,deque
input = sys.stdin.readline
    
def BFS(graph, x, y):# 출발 노드 : x, 도착노드 : y
    
    
    visited = [False] * (N+1) # 맨앞에 0번쨰 자리는 제외하므로 n+1을 해줘야 원래수대로 쓸수있다.
    que = deque()
    que.append(x)
    visited[x] = True  # 방문했다는 표시
    target_dist = [0]*(N+1) # index : nord, value : index 노드까지의 거리
    
    while que : # 출발노드부터 시작해서 방문 노드 que에넣기 
        v = que.popleft() # 현재 노드 빼서 v에넣기 
        if v == y:   # 목표노드에 도착  
            print(target_dist[v])
            return 
        for next,dist in graph[v] :
            if not visited[next] : # 방문 여부 확인
                que.append(next) # que에 추가
                visited[next] = True
                target_dist[next] += target_dist[v] + dist #거리더하기
    
    
def nord():
    global N,M
    N,M = map(int,input().split()) #노드개수 N개 , 거리를 구해야하는 수 M개
    graph = defaultdict(list)
    
    for _ in range(N-1):
        a,b,dist = map(int,input().split())
        graph[a].append((b,dist))
        graph[b].append((a,dist))
            

    for _ in range(M):
        a,b = map(int,input().split())
        BFS(graph,a,b)
    

    
if __name__ == "__main__" :
    nord()