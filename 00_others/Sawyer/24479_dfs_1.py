import sys

def dfs(E, R, visited) :  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    print(R)
    global count
    count +=1
    visited[R] = True  # 시작 정점 R을 방문 했다고 표시한다.
    for x in E[R]:  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if visited[x] == False :
            dfs(E, x, visited)
        
            

def dfs_1() :
    global count
    count = 0
    N,M,R = map(int,sys.stdin.readline().split())
    E = [[] for _ in range(N+1)]
    
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        
        E[a].append(b)
        E[b].append(a)
        
    for i in range(1, N+1):
        E[i].sort()
    
    
    visited = [False for _ in range(N+1)]
    
    dfs(E, R, visited)
    
    
    if len(E) - 1 >count :
        print(0)
        
  
    
if __name__ == "__main__" :
    dfs_1()