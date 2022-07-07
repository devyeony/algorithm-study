import sys
from collections import deque


def tomato():
    input = sys.stdin.readline
    M,N = map(int, input().split())
    
    
    data = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    
    for i in range(N) :
        for j in range(M) :
            if data[i][j] == 1:
                queue.append((i,j))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1<nx<N and -1<ny<M :
                if data[nx][ny] == 0 :
                    data[nx][ny] = data[x][y] + 1
                    queue.append((nx,ny))
                    
            
    flag = 0
    result = -2
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                flag = 1
                
            result = max(result,data[i][j])
            
    
    
    if flag == 1:
        print(-1)
    elif result == -1 :
        print(0)
    else :
        print(result-1)
       
    
    




if __name__ == "__main__" :
    tomato()