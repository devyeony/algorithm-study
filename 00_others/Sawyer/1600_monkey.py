import sys
from collections import deque()
input = sys.stdin.readline

def BFS(graph,x,y):
    
    visited[0][0] = True
    dx = [0,1]
    dy = [-1,0]
    que = deque([x,y])
    
    horse = [[2,-1],[-1,2]]
    

    while que :
         = que.popleft()
    
def monkey():
    K = int(input())
    W, H = map(int,input().split())
    
    graph = [list(map(int,input().split())) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    
    x,y = 0,0
    
    BFS(graph,visited,x,y)
    
    
if __name__ == "__main__" :
    monkey()
    