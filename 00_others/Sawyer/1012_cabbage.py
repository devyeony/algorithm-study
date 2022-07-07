import sys
from collections import deque


def BFS(graph,x,y):
     
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    graph[x][y] = 0
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx< M and 0<=ny<N and graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append([nx, ny])
    
    return


def cabbage():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        global N,M
        M,N,K = map(int,sys.stdin.readline().split()) # M은 가로 N은 세로
        graph = [[0] * N for i in range(M)]
        for i in range(K):
            a,b = map(int,sys.stdin.readline().split())
            graph[a][b] = 1

        count = 0
        for i in range(M):
            for j in range(N):
                if graph[i][j] == 1:
                    BFS(graph,i,j)
                    count += 1
        print(count)
            
if __name__ == "__main__":
    cabbage()
    
    
    
    
    